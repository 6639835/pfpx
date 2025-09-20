# Airways and Routes

Airways define the route structure connecting waypoints for aircraft navigation. They specify altitude constraints, routing, and operational parameters.

> **📍 Looking for sector altitude constraints or cruise data?** See **[Cruise Tables](./cruise-table.md)** for FIR sectors, heading ranges, and altitude restrictions.

## Format Structure

```
AWY ROUTEAA#SSSSSSEEEEEEDDDDD±LLLLLLLLL±LLLLLLLLL±LLLLLLLLL±LLLLLLLLLMMMMMMMMMMMMR
```

## Example Record

```
AWY A461  FA30980180980530+22543333+114133333+22896389+113951667NESTBUNLTD1
```

## Field Breakdown

### Basic Information
| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `AWY` | Airway identifier | Fixed value indicating this record is an airway |
| `A461` | Airway designation | Route designation |
| `FA` | Cruise identifier | See [Cruise Tables](./cruise-table.md) |
| `3` | Airway type | 1=High, 2=Low, 3=Both |
| `098018` | Start waypoint database ID |  |
| `098053` | End waypoint database ID |  |
| `0` | Direction flag | 1=Bidirectional, 0=Unidirectional |
| `+22543333` | Start point latitude |  |
| `+114133333` | Start point longitude |  |
| `+22896389` | End point latitude |  |
| `+113951667` | End point longitude |  |
| `NESTB` | Lower altitude | Lower limit or "NESTB" for no lower limit |
| `UNLTD` | Upper altitude | Upper limit or "UNLTD" for unlimited |
| `1` | Navigation type | 1=RNAV, 0=Conventional |

## Altitude Encoding

### Special Values
- **NESTB** - No established lower limit
- **UNLTD** - Unlimited upper altitude
- **Numeric** - Specific altitude in feet or flight level

### Format Examples
```
04500  → 4,500 feet MSL
FL290  → Flight Level 290 (29,000 feet)
NESTB  → No lower limit established
UNLTD  → No upper limit
```

## Route Types

| Code | Description | Usage |
|------|-------------|-------|
| 1 | High Altitude | FL180 and above |
| 2 | Low Altitude | Below FL180 |
| 3 | High/Low | Both altitude ranges |

## Direction Codes

| Code | Description | Restrictions |
|------|-------------|--------------|
| 0 | Unidirectional | One-way routing |
| 1 | Bidirectional | Two-way routing |

## Programming Examples

### Python Parser

```python
import re

def parse_airway(line):
    """Parse an airway record."""
    # AWY A461  FA30980180980530+22543333+114133333+22896389+113951667NESTBUNLTD1
    pattern = r'AWY (\w+)\s+(\w{2})(\d)(\d{6})(\d{6})(\d)([+-]\d{8})([+-]\d{9})([+-]\d{8})([+-]\d{9})(\w+)(\w+)(\d)'
    
    match = re.match(pattern, line)
    if match:
        return {
            'route_id': match.group(1),
            'region': match.group(2),
            'route_type': int(match.group(3)),
            'start_waypoint_id': match.group(4),
            'end_waypoint_id': match.group(5),
            'direction': int(match.group(6)),
            'start_lat': int(match.group(7)) / 1_000_000,
            'start_lon': int(match.group(8)) / 1_000_000,
            'end_lat': int(match.group(9)) / 1_000_000,
            'end_lon': int(match.group(10)) / 1_000_000,
            'min_altitude': match.group(11),
            'max_altitude': match.group(12),
            'rnav': bool(int(match.group(13)))
        }
    return None

# Usage
airway = parse_airway("AWY A461  FA30980180980530...")
print(f"Route {airway['route_id']}: {airway['start_lat']},{airway['start_lon']} to {airway['end_lat']},{airway['end_lon']}")
```

### Route Network Analysis

```python
from collections import defaultdict

def build_route_network(airway_lines):
    """Build a network graph from airway data."""
    network = defaultdict(list)
    
    for line in airway_lines:
        if line.startswith('AWY'):
            airway = parse_airway(line)
            if airway:
                # Add route segment
                start = (airway['start_lat'], airway['start_lon'])
                end = (airway['end_lat'], airway['end_lon'])
                
                network[start].append({
                    'destination': end,
                    'route': airway['route_id'],
                    'min_alt': airway['min_altitude'],
                    'max_alt': airway['max_altitude']
                })
                
                # Add reverse if bidirectional
                if airway['direction'] == 1:
                    network[end].append({
                        'destination': start,
                        'route': airway['route_id'],
                        'min_alt': airway['min_altitude'],
                        'max_alt': airway['max_altitude']
                    })
    
    return dict(network)
```

## Altitude Validation

```python
def parse_altitude_limit(alt_string):
    """Parse altitude limit string."""
    if alt_string == "NESTB":
        return None, "no_lower_limit"
    elif alt_string == "UNLTD":
        return None, "unlimited"
    elif alt_string.startswith("FL"):
        # Flight level
        fl = int(alt_string[2:])
        return fl * 100, "flight_level"
    else:
        # Feet MSL
        return int(alt_string), "msl"

def validate_altitude_range(min_alt, max_alt, aircraft_altitude):
    """Check if aircraft altitude is within airway limits."""
    min_val, min_type = parse_altitude_limit(min_alt)
    max_val, max_type = parse_altitude_limit(max_alt)
    
    # Check lower limit
    if min_val is not None and aircraft_altitude < min_val:
        return False, f"Below minimum altitude {min_alt}"
    
    # Check upper limit  
    if max_val is not None and aircraft_altitude > max_val:
        return False, f"Above maximum altitude {max_alt}"
    
    return True, "Within limits"
```

## Route Planning Applications

### Find Route Segments

```python
def find_route_segments(network, route_id):
    """Find all segments for a specific route."""
    segments = []
    
    for start_point, connections in network.items():
        for connection in connections:
            if connection['route'] == route_id:
                segments.append({
                    'start': start_point,
                    'end': connection['destination'],
                    'min_alt': connection['min_alt'],
                    'max_alt': connection['max_alt']
                })
    
    return segments

# Usage
a461_segments = find_route_segments(network, "A461")
print(f"Route A461 has {len(a461_segments)} segments")
```

### Altitude Planning

```python
def plan_route_altitudes(route_segments, requested_altitude):
    """Check altitude compatibility along route."""
    issues = []
    
    for i, segment in enumerate(route_segments):
        valid, message = validate_altitude_range(
            segment['min_alt'], 
            segment['max_alt'], 
            requested_altitude
        )
        
        if not valid:
            issues.append({
                'segment': i,
                'start': segment['start'],
                'end': segment['end'],
                'issue': message
            })
    
    return issues
```

## Data Integration

Airways connect to other navdata sections:

- **[Waypoints](./waypoints.md)**: Start/end points of route segments
- **[SID Procedures](./sid-procedures.md)**: Connect to airway system
- **[STAR Procedures](./star-procedures.md)**: Connect from airway system

## Next Steps

- **[Learn about SID procedures](./sid-procedures.md)** - How departures connect to airways
- **[Explore STAR procedures](./star-procedures.md)** - How arrivals use airways
- **[Use analysis tools](../tools/examples.md)** - Extract and analyze airway data
