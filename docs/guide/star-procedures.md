# STAR Procedures (Standard Terminal Arrivals)

Standard Terminal Arrival Route (STAR) procedures provide standardized routing from the enroute structure to airports. Each STAR consists of multiple waypoints that define the arrival path.

## Format Structure

```
STR ICAORRR  DDDDDDWWWWWWNNNNNPPPPPPTTTTTTT ±LLLLLLLLL±LLLLLLLLLS
```

## Example Records

```
STR YWLMALL  319972094283EKIPUIVTA1REKIPU -33207250+1517406671
STR YWLMALL  319973258035IVTAGIVTA1REKIPU -33038028+1517578331
STR YWLMALL  319974094930OVLUXIVTA1ROVLUX -33173056+1516178061
STR YWLMALL  319975258035IVTAGIVTA1ROVLUX -33038028+1517578331
STR YWLMALL  319976095000PUDUTIVTA1RPUDUT -32961389+1514733061
STR YWLMALL  319977258035IVTAGIVTA1RPUDUT -33038028+1517578331
STR YWLM30   319978258035IVTAGIVTA1R      -33038028+1517578331
STR YWLM30   319979258061UBGIMIVTA1R      -32942194+1518618331
```

## Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `STR` | Arrival procedure identifier | Fixed value indicating this record is a STAR |
| `YWLM` | ICAO code |  |
| `ALL` | Runway designation | ALL = All runways; xxB = xxL / xxC / xxR |
| `319972` | STAR database ID |  |
| `094283` | Waypoint ID (current line) |  |
| `EKIPU` | Waypoint name (current line) |  |
| `IVTA1R` | Procedure identifier |  |
| `EKIPU` | Procedure transition point | If transition point exists, its name is filled in |
| `+40073450` | Latitude (current waypoint) |  |
| `+116574192` | Longitude (current waypoint) |  |
| `1` | RNAV procedure flag | 0 = No, 1 = Yes |

## Runway Designations

### Format Examples
- **Specific Runway**: `30`, `12`, `06R` - Applies to single runway
- **Multiple Runways**: `ALL` - Applies to all runways  
- **Grouped Runways**: `36B` - Applies to 36L/36C/36R


## Programming Examples

### Python Parser

```python
import re

def parse_star(line):
    """Parse a STAR procedure record."""
    # STR YWLMALL  319972094283EKIPUIVTA1REKIPU -33207250+1517406671
    pattern = r'STR (\w{4})(\w+)\s+(\d{6})(\d{6})(\w+)(\w+)(\w+) ([+-]\d{8,9})([+-]\d{8,9})(\d)'
    
    match = re.match(pattern, line)
    if match:
        return {
            'airport': match.group(1),
            'runway': match.group(2),
            'procedure_id': match.group(3),
            'waypoint_id': match.group(4),
            'waypoint_name': match.group(5),
            'star_name': match.group(6),
            'transition': match.group(7),
            'latitude': int(match.group(8)) / 1_000_000,
            'longitude': int(match.group(9)) / 1_000_000,
            'rnav': bool(int(match.group(10)))
        }
    return None

# Usage
star = parse_star("STR YWLMALL  319972094283EKIPUIVTA1REKIPU...")
print(f"STAR {star['star_name']} to {star['airport']} runway {star['runway']}")
```

### Build Arrival Routes

```python
from collections import defaultdict

def build_star_routes(star_lines):
    """Build complete STAR routes from individual records."""
    procedures = defaultdict(list)
    
    for line in star_lines:
        if line.startswith('STR'):
            star = parse_star(line)
            if star:
                # Group by procedure and transition
                key = f"{star['airport']}-{star['runway']}-{star['star_name']}-{star['transition']}"
                procedures[key].append(star)
    
    # Sort waypoints by procedure ID (sequential order)
    for key in procedures:
        procedures[key].sort(key=lambda x: x['procedure_id'])
    
    return dict(procedures)
```

### Analyze Arrival Flows

```python
def analyze_arrival_flows(star_lines, airport_icao):
    """Analyze arrival patterns for an airport."""
    arrival_data = {
        'transitions': defaultdict(set),
        'runway_stars': defaultdict(set),
        'total_procedures': 0
    }
    
    for line in star_lines:
        if line.startswith('STR'):
            star = parse_star(line)
            if star and star['airport'] == airport_icao:
                # Track transitions
                arrival_data['transitions'][star['transition']].add(star['star_name'])
                
                # Track runway assignments
                arrival_data['runway_stars'][star['runway']].add(star['star_name'])
                
                arrival_data['total_procedures'] += 1
    
    return arrival_data

# Usage
flows = analyze_arrival_flows(star_lines, "YWLM")
print(f"Arrival analysis for {airport_icao}")
for transition, stars in flows['transitions'].items():
    print(f"Transition {transition}: {', '.join(stars)}")
```

## Route Continuity

### Initial Approach Fix Definition
The first waypoint in each STAR defines the entry point:

```python
def find_initial_approach_fixes(star_routes):
    """Find initial approach fixes for STAR procedures."""
    iaf_points = {}
    
    for route_key, waypoints in star_routes.items():
        if waypoints:
            # First waypoint is the IAF
            first_waypoint = min(waypoints, key=lambda x: x['procedure_id'])
            iaf_points[route_key] = {
                'name': first_waypoint['waypoint_name'],
                'latitude': first_waypoint['latitude'],
                'longitude': first_waypoint['longitude']
            }
    
    return iaf_points
```

### Multiple Runway Routing

STAR procedures often serve multiple runways with different final segments:

```python
def group_stars_by_runway(star_routes):
    """Group STAR routes by destination runway."""
    runway_groups = defaultdict(list)
    
    for route_key, waypoints in star_routes.items():
        # Extract runway from route key
        airport, runway, star_name, transition = route_key.split('-')
        runway_groups[runway].append({
            'star_name': star_name,
            'transition': transition,
            'waypoints': waypoints
        })
    
    return dict(runway_groups)
```

## Validation and Analysis

### Route Validation

```python
def validate_star_sequence(waypoints):
    """Validate STAR waypoint sequence."""
    issues = []
    
    if not waypoints:
        return ["No waypoints found"]
    
    # Check for proper sequencing
    ids = [wp['procedure_id'] for wp in waypoints]
    if ids != sorted(ids):
        issues.append("Waypoints not in sequential order")
    
    # Check for reasonable distances
    for i in range(len(waypoints) - 1):
        wp1 = waypoints[i]
        wp2 = waypoints[i + 1]
        
        distance = calculate_distance(
            wp1['latitude'], wp1['longitude'],
            wp2['latitude'], wp2['longitude']
        )
        
        if distance > 200:  # More than 200 nm between waypoints
            issues.append(f"Large gap between {wp1['waypoint_name']} and {wp2['waypoint_name']}: {distance:.1f}nm")
    
    return issues
```

### Transition Analysis

```python
def analyze_star_transitions(star_routes):
    """Analyze STAR transition patterns."""
    transition_stats = defaultdict(lambda: {
        'count': 0,
        'airports': set(),
        'runways': set()
    })
    
    for route_key, waypoints in star_routes.items():
        airport, runway, star_name, transition = route_key.split('-')
        
        stats = transition_stats[transition]
        stats['count'] += 1
        stats['airports'].add(airport)
        stats['runways'].add(f"{airport}-{runway}")
    
    # Convert sets to lists for display
    result = {}
    for transition, stats in transition_stats.items():
        result[transition] = {
            'count': stats['count'],
            'airports': list(stats['airports']),
            'runways': list(stats['runways'])
        }
    
    return result
```

## Integration with Other Data

### Connection to Airways

```python
def find_star_airway_connections(star_routes, airway_data):
    """Find connections between STARs and airways."""
    connections = []
    
    for route_key, star_waypoints in star_routes.items():
        if not star_waypoints:
            continue
            
        # Get initial approach fix
        iaf = min(star_waypoints, key=lambda x: x['procedure_id'])
        iaf_pos = (iaf['latitude'], iaf['longitude'])
        
        # Find nearby airway endpoints
        for airway in airway_data:
            airway_end = (airway['end_lat'], airway['end_lon'])
            
            distance = calculate_distance(
                iaf_pos[0], iaf_pos[1],
                airway_end[0], airway_end[1]
            )
            
            if distance < 5:  # Within 5nm
                connections.append({
                    'star': route_key,
                    'airway': airway['route_id'],
                    'distance': distance,
                    'connection_point': iaf['waypoint_name']
                })
    
    return connections
```

## Special Cases

### Route Segment Starting Point Definition
Each STR procedure must define the route segment starting point in the first line

Example:

```
STR ZGSZALL  322166098018BEKOLBEK1XA      +22543333+1141333330
STR ZGSZ15   322167098018BEKOLBEK1XA      +22543333+1141333330
STR ZGSZ15   322168259574CEN45BEK1XA      +22691161+1140501530
STR ZGSZ16   322169098018BEKOLBEK1XA      +22543333+1141333330
STR ZGSZ16   322170259574CEN45BEK1XA      +22691161+1140501530
```

> `BEKOL` indicates the starting point of this arrival procedure

### Different Runway Segments
If the same arrival procedure corresponds to multiple runways, all segments need to be listed separately according to runway designation

Example:

```
STR ZBAAALL  320182097915OSUBAOSUB7X      +40736389+1170372221
STR ZBAAALL  320183258281AA169OSUB7X      +40680611+1169732221
STR ZBAAALL  320184258278AA166OSUB7X      +40419722+1166791671
STR ZBAAALL  320185258277AA165OSUB7X      +40119222+1167258061
STR ZBAAALL  320186258264AA142OSUB7X      +40038056+1167383331
STR ZBAA01   320187258264AA142OSUB7X      +40038056+1167383331
STR ZBAA01   320188258263AA141OSUB7X      +39685972+1167923891
STR ZBAA36B  320189258264AA142OSUB7X      +40038056+1167383331
STR ZBAA36B  320190258263AA141OSUB7X      +39685972+1167923891
```

## Data Integration

STAR procedures connect to other navdata sections:

- **[Airways](./airways.md)**: Entry points from enroute structure
- **[Waypoints](./waypoints.md)**: Navigation points in STAR routes
- **[Runways](./runways.md)**: Destination runways for arrivals

## Next Steps

- **[Review SID procedures](./sid-procedures.md)** - Departure procedure complement
- **[Understand waypoints](./waypoints.md)** - STAR navigation points
- **[Use analysis tools](../tools/examples.md)** - Extract and analyze STAR data

## Summary

STAR procedures provide structured arrival routing that:

- **Standardizes** arrival flows into airports
- **Reduces** pilot and controller workload  
- **Improves** efficiency and safety
- **Connects** enroute structure to terminal areas
- **Supports** both conventional and RNAV navigation
