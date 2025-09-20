# SID Procedures (Standard Instrument Departures)

Standard Instrument Departure (SID) procedures provide standardized routing from airports to the enroute structure. Each SID consists of multiple waypoints that define the departure path.

## Format Structure

```
SID ICAORRR  DDDDDDWWWWWWNNNNNPPPPPPTTTTTTT ±LLLLLLLLL±LLLLLLLLLS
```

## Example Records

```
SID RJNAALL  101992213869TALMITALMI4KAMMY +35471000+1366238140
SID RJNAALL  101993213858HEIANTALMI4KAMMY +35346375+1357621190
SID RJNAALL  101994075088KAMMYTALMI4KAMMY +34991006+1346885330
SID RJNAALL  101995213869TALMITALMI4PIONE +35471000+1366238140
SID RJNAALL  101996213858HEIANTALMI4PIONE +35346375+1357621190
SID RJNAALL  101997075867WAKITTALMI4PIONE +35032736+1349255530
SID RJNAALL  101998075515PIONETALMI4PIONE +34671378+1340151310
SID RJNAALL  101999213869TALMITALMI4WAKIT +35471000+1366238140
SID RJNAALL  102000213858HEIANTALMI4WAKIT +35346375+1357621190
SID RJNAALL  102001075867WAKITTALMI4WAKIT +35032736+1349255530
```

## Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `SID` | Departure procedure identifier | Fixed value indicating this record is a SID |
| `RJNA` | ICAO code |  |
| `ALL` | Runway designation | ALL = All runways; xxB = xxL / xxC / xxR |
| `101992` | SID database ID |  |
| `213869` | Waypoint ID (current line) |  |
| `TALMI` | Waypoint name (current line) |  |
| `TALMI4` | Procedure identifier |  |
| `KAMMY` | Procedure transition point | If transition point exists, its name is filled in |
| `+40073450` | Latitude (current waypoint) |  |
| `+116574192` | Longitude (current waypoint) |  |
| `0` | RNAV procedure flag | 0 = No, 1 = Yes |

## Runway Designations

### Standard Format
- **Specific Runway**: `01`, `36`, `27L` - Applies to single runway
- **Multiple Runways**: `ALL` - Applies to all runways
- **Grouped Runways**: `36B` - Applies to 36L/36C/36R

### Examples
```
SID ZBAA01   ... → Runway 01 specific
SID ZBAAALL  ... → All runways
SID ZBAA36B  ... → Runways 36L, 36C, 36R
```

## Programming Examples

### Python Parser

```python
import re

def parse_sid(line):
    """Parse a SID procedure record."""
    # SID RJNAALL  101992213869TALMITALMI4KAMMY +35471000+1366238140
    pattern = r'SID (\w{4})(\w+)\s+(\d{6})(\d{6})(\w+)(\w+)(\w+) ([+-]\d{8,9})([+-]\d{8,9})(\d)'
    
    match = re.match(pattern, line)
    if match:
        return {
            'airport': match.group(1),
            'runway': match.group(2),
            'procedure_id': match.group(3),
            'waypoint_id': match.group(4),
            'waypoint_name': match.group(5),
            'sid_name': match.group(6),
            'transition': match.group(7),
            'latitude': int(match.group(8)) / 1_000_000,
            'longitude': int(match.group(9)) / 1_000_000,
            'rnav': bool(int(match.group(10)))
        }
    return None

# Usage
sid = parse_sid("SID RJNAALL  101992213869TALMITALMI4KAMMY...")
print(f"SID {sid['sid_name']} from {sid['airport']} runway {sid['runway']}")
```

### Build Procedure Routes

```python
from collections import defaultdict

def build_sid_routes(sid_lines):
    """Build complete SID routes from individual records."""
    procedures = defaultdict(list)
    
    for line in sid_lines:
        if line.startswith('SID'):
            sid = parse_sid(line)
            if sid:
                # Group by procedure and transition
                key = f"{sid['airport']}-{sid['runway']}-{sid['sid_name']}-{sid['transition']}"
                procedures[key].append(sid)
    
    # Sort waypoints by procedure ID (sequential order)
    for key in procedures:
        procedures[key].sort(key=lambda x: x['procedure_id'])
    
    return dict(procedures)
```

### Extract Waypoint Sequence

```python
def get_waypoint_sequence(sid_route):
    """Extract ordered waypoint sequence for a SID route."""
    waypoints = []
    
    for waypoint in sorted(sid_route, key=lambda x: x['procedure_id']):
        waypoints.append({
            'name': waypoint['waypoint_name'],
            'latitude': waypoint['latitude'],
            'longitude': waypoint['longitude'],
            'sequence': len(waypoints) + 1
        })
    
    return waypoints

# Usage
routes = build_sid_routes(sid_lines)
for route_key, route_data in routes.items():
    waypoints = get_waypoint_sequence(route_data)
    print(f"Route {route_key}:")
    for wp in waypoints:
        print(f"  {wp['sequence']}. {wp['name']} ({wp['latitude']:.6f}, {wp['longitude']:.6f})")
```

## Analysis Examples

### Airport SID Summary

```python
def analyze_airport_sids(sid_lines, airport_icao):
    """Analyze all SIDs for a specific airport."""
    airport_sids = defaultdict(set)
    
    for line in sid_lines:
        if line.startswith('SID'):
            sid = parse_sid(line)
            if sid and sid['airport'] == airport_icao:
                airport_sids[sid['runway']].add(sid['sid_name'])
    
    print(f"SID Analysis for {airport_icao}")
    print("=" * 40)
    
    for runway in sorted(airport_sids.keys()):
        sids = sorted(airport_sids[runway])
        print(f"Runway {runway}: {', '.join(sids)}")
    
    total_sids = sum(len(sids) for sids in airport_sids.values())
    print(f"\nTotal SIDs: {total_sids}")
    print(f"Runways served: {len(airport_sids)}")

# Usage
analyze_airport_sids(sid_lines, "ZBAA")
```

### Route Distance Calculation

```python
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate great circle distance between two points."""
    R = 3440.065  # Earth radius in nautical miles
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2) 
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = (math.sin(delta_lat/2) * math.sin(delta_lat/2) + 
         math.cos(lat1_rad) * math.cos(lat2_rad) * 
         math.sin(delta_lon/2) * math.sin(delta_lon/2))
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def calculate_sid_distance(waypoint_sequence):
    """Calculate total distance for SID route."""
    total_distance = 0
    
    for i in range(len(waypoint_sequence) - 1):
        wp1 = waypoint_sequence[i]
        wp2 = waypoint_sequence[i + 1]
        
        distance = calculate_distance(
            wp1['latitude'], wp1['longitude'],
            wp2['latitude'], wp2['longitude']
        )
        total_distance += distance
    
    return total_distance
```

## Procedure Validation

### Check Route Continuity

```python
def validate_sid_continuity(waypoint_sequence, max_segment_distance=50):
    """Validate SID route for unrealistic segments."""
    issues = []
    
    for i in range(len(waypoint_sequence) - 1):
        wp1 = waypoint_sequence[i]
        wp2 = waypoint_sequence[i + 1]
        
        distance = calculate_distance(
            wp1['latitude'], wp1['longitude'],
            wp2['latitude'], wp2['longitude']
        )
        
        if distance > max_segment_distance:
            issues.append({
                'segment': f"{wp1['name']} to {wp2['name']}",
                'distance': distance,
                'issue': 'Excessive segment distance'
            })
    
    return issues
```

## Data Integration

SID procedures connect to other navdata sections:

- **[Runways](./runways.md)**: Departure runways for procedures
- **[Waypoints](./waypoints.md)**: Navigation points in SID routes
- **[Airways](./airways.md)**: Connection points to enroute structure

## Special Considerations

### Common Segments
SID common segments

```
STR KF41ALL  199955043375STNLIJFRYE5STNLI +34404792-0994160061
STR KF41ALL  199956043051POTZYJFRYE5STNLI +34018117-0986128611
STR KF41ALL  199957041410BUROZJFRYE5STNLI +33918744-0984093781
STR KF41ALL  199958042672LNDUSJFRYE5STNLI +33604175-0977727781
STR KF41ALL  199959042015GREGSJFRYE5STNLI +33450608-0974660561
STR KF41ALL  199960043540TURKIJFRYE5TURKI +34300925-1010608391
STR KF41ALL  199961041873GANJAJFRYE5TURKI +34204189-1002545281
STR KF41ALL  199962041602DEDWTJFRYE5TURKI +34021694-0992525671
STR KF41ALL  199963044059ZORDAJFRYE5TURKI +33781175-0984901331
STR KF41ALL  199964042015GREGSJFRYE5TURKI +33450608-0974660561
STR KF41ALL  199965044059ZORDAJFRYE5ZORDA +33781175-0984901331
STR KF41ALL  199966042015GREGSJFRYE5ZORDA +33450608-0974660561
STR KF41ALL  199967042015GREGSJFRYE5      +33450608-0974660561
STR KF41ALL  199968042784MNKEEJFRYE5      +33429283-0969174581
STR KF41ALL  199969042291JFRYEJFRYE5      +33389456-0968322331
STR KF41ALL  199970042291JFRYEJFRYE5      +33389456-0968322331
```

Those without transition points are common segments of this procedure

## Next Steps

- **[Learn about STAR procedures](./star-procedures.md)** - Arrival procedure complement
- **[Explore waypoints](./waypoints.md)** - Understanding SID navigation points
- **[Use analysis tools](../tools/examples.md)** - Extract and analyze SID data
