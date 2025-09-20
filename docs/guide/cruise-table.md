# Cruise Tables

Cruise tables contain flight performance and altitude constraint data used for flight planning calculations. These tables provide standardized cruise parameters for different aircraft types and flight conditions.

## Format Structure

```
XX HHH HHH T/M [ALTITUDE_RESTRICTIONS...]
```

Where:
- `XX` = Region code (2 characters)
- `HHH` = Start heading (3 digits)
- `HHH` = End heading (3 digits)
- `T/M` = Heading type (T=True, M=Magnetic)
- `[ALTITUDE_RESTRICTIONS...]` = Altitude restriction data (variable length)

## Example Records

```
AA 360 179 M 010000200029000 2900004000UNLTD                                 
AA 180 359 M 020000200028000 280000300031000 3100004000UNLTD                 
AO 360 179 M 020000200028000 280000300031000 3100004000UNLTD                 
AO 180 359 M 010000200029000 2900004000UNLTD                                 
BA 030 209 M 010000200029000 2900004000UNLTD                                 
BA 210 029 M 020000200028000 280000300031000 3100004000UNLTD                 
BB 030 209 M 010000200041000 4100004000UNLTD                                 
BB 210 029 M 020000200040000 400000300043000 4300004000UNLTD                 
BO 030 209 M 020000200040000 400000300043000 4300004000UNLTD                 
BO 210 029 M 010000200041000 4100004000UNLTD                                 
BZ 030 209 M 010000200041000 4100004000UNLTD                                 
BZ 210 029 M 020000200040000 400000300043000 4300004000UNLTD                 
CA 360 179 T M0090M0060M0810 M0810M0090M0900 M0900M0120M1500                 
CA 180 359 T M0060M0060M0840 M0840M0120M1440                                 
CO 360 179 T M0060M0060M0840 M0840M0120M1440                                 
CO 180 359 T M0090M0060M0810 M0810M0090M0900 M0900M0120M1500                 
CZ 090 269 M 010000100041000 4100002000UNLTD                                 
DA 090 269 M 010000200041000 4100004000UNLTD                                 
DA 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
DO 090 269 M 010000200041000 4100004000UNLTD                                 
DO 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
EA 090 269 M 010000200029000 2900004000UNLTD                                 
EA 270 089 M 020000200028000 280000300031000 3100004000UNLTD                 
EO 270 089 M 010000200029000 2900004000UNLTD                                 
EO 090 269 M 020000200028000 280000300031000 3100004000UNLTD                 
FA 360 179 T M0090M0060M0810 M0810M0080M0890 M0890M0060M1250 M1250M0120M1490 
FA 180 359 T M0060M0060M0840 M0840M0080M0920 M0920M0060M1220 M1220M0090M1310 
FA 180 359 T M1310M0120M1550                                                 
FO 360 179 T M0060M0060M0840 M0840M0080M0920 M0920M0060M1220 M1220M0090M1310 
FO 360 179 T M1310M0120M1550                                                 
FO 180 359 T M0090M0060M0810 M0810M0080M0890 M0890M0060M1250 M1250M0120M1490 
GA 360 179 M 030000190004900 049000200008900 089000190010800 108000200014800 
GA 360 179 M 148000190016700 167000200020700 207000190022600 226000200026600 
GA 360 179 M 266000250029100 291000200041100 411000380044900 449000400048900 
GA 180 359 M 020000190003900 039000200007900 079000190009800 098000200013800 
GA 180 359 M 138000190015700 157000200021700 217000190023600 236000200027600 
GA 180 359 M 276000250030100 301000200040100 401000290043000 430000390046900 
GA 180 359 M 469000400050900                                                 
GO 180 359 M 030000190004900 049000200008900 089000190010800 108000200014800 
GO 180 359 M 148000190016700 167000200020700 207000190022600 226000200026600 
GO 180 359 M 266000250029100 291000200041100 411000380044900 449000400048900 
GO 360 179 M 020000190003900 039000200007900 079000190009800 098000200013800 
GO 360 179 M 138000190015700 157000200021700 217000190023600 236000200027600 
GO 360 179 M 276000250030100 301000200040100 401000290043000 430000390046900 
GO 360 179 M 469000400050900                                                 
IZ 090 269 M 020000200040000 400000300043000 4300004000UNLTD                 
IZ 270 089 M 010000200041000 4100004000UNLTD                                 
KA 360 179 T M0090M0060M0810 M0810M0100M1210 M1210M0200M1610                 
KA 180 359 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
KA 180 359 T M1310M0200M1510                                                 
KO 180 359 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
KO 180 359 T M1310M0200M1510                                                 
KO 360 179 T M0090M0060M0810 M0810M0100M1210 M1210M0200M1610                 
NA 360 089 M 030000200013000 150000200029000 2900004000UNLTD                 
NA 090 179 M 035000200013500 150000200029000 2900004000UNLTD                 
NA 180 269 M 040000200012000 160000200028000 280000300031000 3100004000UNLTD 
NA 270 359 M 045000200012500 160000200028000 280000300031000 3100004000UNLTD 
OY 360 179 M 010003200033000 330001200045000 4500004000UNLTD                 
OY 180 359 M 020002800030000 300001300043000 4300004000UNLTD                 
PB 180 359 M 200000200032000 320000100041000                                 
PC 180 359 M 200000200034000 340000100038000 380000200040000 400000100041000 
PD 360 179 M 190000200029000 290000100035000 350000200041000                 
PE 360 179 M 010000200029000 290000800037000 3700004000UNLTD                 
PE 180 359 M 020000200028000 280000700035000 3500004000UNLTD                 
PF 180 359 M 030000200023000 230000600029000 290000800037000                 
PF 360 179 M 020000200024000 240000400028000 280000600034000                 
PG 360 179 M 020000200024000 240000400028000 280000600034000                 
PG 180 359 M 030000200023000 230000600029000 290000800037000                 
PH 360 179 M 010000200027000 270000400031000 310000200041000 4100004000UNLTD 
PH 180 359 M 280000400032000 320000200040000                                 
PI 360 179 M 010000200041000 4100004000UNLTD                                 
PI 180 359 M 300000600036000                                                 
PJ 360 179 M 010000200027000 270000400031000 310000100032000 320000300035000 
PJ 360 179 M 350000100036000 360000300039000 390000100040000 400000500045000 
PJ 360 179 M 4500004000UNLTD                                                 
PJ 180 359 M 020000200028000 280000300031000 310000100032000 320000300035000 
PJ 180 360 M 350000100036000 360000300039000 390000100040000 400000300043000 
PJ 180 359 M 4300004000UNLTD                                                 
PK 360 179 M 010000200029000 290000400037000 370000200041000 4100004000UNLTD 
PK 180 359 M 020000200030000 300000400038000 380000200040000 400000300043000 
PK 180 359 M 4300004000UNLTD                                                 
PL 360 179 M 010000200027000 270000600033000 3300004000UNLTD                 
PL 180 359 M 020000200028000 280000600034000 340000900043000 4300004000UNLTD 
PM 360 179 M 010000200027000 270000600033000 330001200045000 4500004000UNLTD 
PM 180 359 M 020000200026000 260000400030000 300001300043000 4300004000UNLTD 
PN 360 179 M 010000200029000 290000800045000 4500004000UNLTD                 
PN 180 359 M 020000200028000 280000600034000 340000900043000 4300004000UNLTD 
PO 360 179 M 010000200027000 270000600033000 330000800041000 4100004000UNLTD 
PO 180 359 M 020000200030000 300000800038000 380000500043000 4300004000UNLTD 
PQ 360 179 M 010000200027000 270000600033000 330000800041000 4100004000UNLTD 
PQ 180 359 M 020000200028000 280000500033000 330000800041000 410000200043000 
PQ 180 359 M 4300004000UNLTD                                                 
PR 360 179 M 010000200031000 310000600037000 370000800045000 4500004000UNLTD 
PR 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
PT 360 179 M 010000200041000 4100004000UNLTD                                 
PT 180 359 M 020000200026000 260000400038000 380000500043000 4300004000UNLTD 
PU 360 179 M 010000200027000 270000400039000 390000600045000 4500004000UNLTD 
PU 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
PV 360 179 M 010000200029000 290000400033000 330001200045000 4500004000UNLTD 
PV 180 359 M 020000200026000 260000400038000 380000500043000 4300004000UNLTD 
PW 360 179 M 010000200027000 270000300030000 300000800038000 380000700045000 
PW 360 179 M 4500004000UNLTD                                                 
PW 180 359 M 020000200026000 260000400030000 300000800038000 380000500043000 
PW 180 359 M 4500004000UNLTD                                                 
PX 360 179 M 010000200027000 270000400039000 390000600045000 4500004000UNLTD 
PX 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
PY 360 179 M 030000200027000 270000400039000 390000600045000 4500004000UNLTD 
PY 180 359 M 020000200028000 280000400036000 360000200040000 400000300043000 
PY 180 359 M 4300004000UNLTD                                                 
PZ 360 179 M 010000200029000 290000400037000 370000800045000 4500004000UNLTD 
PZ 180 359 M 020000200026000 260000400038000 380000500043000 4300004000UNLTD 
QB 360 179 M 020000200024000 240000900033000 330001000043000 4300004000UNLTD 
QB 180 359 M 010000200025000 250000100026000 260000400030000 300000800038000 
QB 180 359 M 380000700045000 4500004000UNLTD                                 
QC 360 179 M 010000200027000 270000800035000 350000400039000 390000600045000 
QC 360 179 M 4500004000UNLTD                                                 
QC 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
QD 360 179 M 010000200025000 250000100026000 260000400030000 300000800038000 
QD 360 179 M 380000700045000 4500004000UNLTD                                 
QD 180 359 M 020000200024000 240000300027000 270000600033000 330001000043000 
QD 180 359 M 4300004000UNLTD                                                 
QE 360 179 M 010000200027000 270001100038000 380000500043000                 
QE 180 359 M 020000200028000 280001000038000                                 
QF 360 179 M 010000200025000 250000700032000 320000400036000 360000200038000 
QF 360 179 M 380000700045000 4500004000UNLTD                                 
QF 180 359 M 020000200024000 240000700031000 3100004000UNLTD                 
QO 360 179 M 220000200028000 280000300031000 3100004000UNLTD                 
QO 180 359 M 210000200029000 2900004000UNLTD                                 
RA 360 179 T M0090M0060M0810 M0810M0100M1210 M1210M0200UNLTD                 
RA 180 359 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
RA 180 359 T M1310M0200UNLTD                                                 
RO 360 179 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
RO 360 179 T M1310M0200UNLTD                                                 
RO 180 359 T M0090M0060M0810 M0810M0100M1210 M1210M0200UNLTD                 
SA 360 179 M 010000200041000 4100004000UNLTD                                 
SA 180 359 M 020000200040000 400000300043000 4300004000UNLTD                 
SO 360 179 M 020000200040000 400000300043000 4300004000UNLTD                 
SO 180 359 M 010000200041000 4100004000UNLTD                                 
TA 360 179 M M0090M0060M0570 210000200029000 2900004000UNLTD                 
TA 180 359 M M0120M0060M0600 220000200028000 280000300031000 3100004000UNLTD 
UA 360 179 M 010000200027000 270000300030000 300000400038000 380000500043000 
UA 360 179 M 4300004000UNLTD                                                 
UA 180 359 M 020000200026000 260000300029000 2900004000UNLTD                 
UB 360 179 M 010000200029000 2900004000UNLTD                                 
UB 180 359 M 020000200030000 300000400038000 380000500043000 4300004000UNLTD 
UC 360 179 M 010000200027000 270000300030000 300000400038000 380000700045000 
UC 360 179 M 4500004000UNLTD                                                 
UC 180 359 M 020000200026000 260000500031000 310000100032000 320000300035000 
UC 180 359 M 350000100036000 360000300039000 390000100040000 400000300043000 
UC 180 359 M 4300004000UNLTD                                                 
VA 090 269 M 020000200040000 400000300043000 4300004000UNLTD                 
VA 270 089 M 010000200041000 4100004000UNLTD                                 
VB 360 179 M 010000200027000 270001800045000 4500004000UNLTD                 
VB 180 359 M 020000200028000 280000400032000 320000200034000 340000900043000 
VC 360 179 M 290001200041000                                                 
VC 180 359 M 300001000040000                                                 
VO 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
VO 090 269 M 010000200041000 4100004000UNLTD                                 
VV 000 179 M 020000200028000 290000200041000 4100004000UNLTD                 
VV 180 359 M 010000200027000 300000200040000 400000300043000 4300004000UNLTD 
WA 360 179 T 010000200041000 4100004000UNLTD                                 
WA 180 359 T 020000200040000 400000300043000 4300004000UNLTD                 
WO 360 179 T 020000200040000 400000300043000 4300004000UNLTD                 
WO 180 359 T 010000200041000 4100004000UNLTD                                 
YO 090 269 M 020000200040000 400000300043000 4300004000UNLTD                 
YO 270 089 M 010000200041000 4100004000UNLTD                                 
YY 090 269 M 010000200041000 4100004000UNLTD                                 
YY 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
ZA 090 269 M 040000200012000 120000400016000 160000200040000 400000300043000 
ZA 090 269 M 430000400047000                                                 
ZA 270 089 M 030000200041000 410000400045000                                 
```

## Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `FA` | Cruise identifier | Fixed value indicating this record contains cruise performance data |
| `360` | Heading | ICAO aircraft type designator |
| `179` | Heading | Standard flight level (FL350 = 35,000 feet) |
| `T` | Magnetic indicator | T=True, M=Magnetic |
| `M0090M0060M0810` | Cruise altitude layer identifier | From 900M to 8100M with RVSM interval of 600M |
| `M0810M0080M0890` | Cruise altitude layer identifier | From 8100M to 8900M with RVSM interval of 800M |
| `M0890M0060M1250` | Cruise altitude layer identifier | From 8900M to 12500M with RVSM interval of 600M |
| `M1250M0120M1490` | Cruise altitude layer identifier | From 12500M to 14900M with RVSM interval of 1200M |

## Notes

In the examples, altitude layers like `010000200027000` use feet as the unit if not prefixed with M. In this example, it means: from 10000FT to 27000FT with RVSM interval of 2000FT.

## Heading Ranges

### Standard Format
- **Full Coverage**: `000 359` - Applies to all headings (360-degree full coverage)
- **Semicircle Range**: `360 179` - Applies to northern semicircle (360°-179°)
- **Semicircle Range**: `180 359` - Applies to southern semicircle (180°-359°)
- **Quadrant Range**: `090 269` - Applies to eastern semicircle (090°-269°)

### Magnetic Declination Indicator
- **T (True)**: True heading, based on geographic north pole
- **M (Magnetic)**: Magnetic heading, based on magnetic north pole

## Altitude Restriction Encoding

### RVSM Interval System
The RVSM (Reduced Vertical Separation Minimum) system defines intervals for different altitude layers:

```python
def parse_altitude_restrictions(altitude_string):
    """Parse altitude restriction string."""
    import re
    
    # Detect if using metric units
    if altitude_string.startswith('M'):
        unit = 'meters'
        altitude_string = altitude_string[1:]  # Remove M prefix
    else:
        unit = 'feet'
    
    # Parse altitude range pattern: start_altitude+interval+end_altitude
    pattern = r'(\d{4,5})(\d{2,4})(\d{4,5})'
    matches = re.findall(pattern, altitude_string)
    
    altitude_ranges = []
    for match in matches:
        start_alt = int(match[0])
        interval = int(match[1])
        end_alt = int(match[2])
        
        altitude_ranges.append({
            'start_altitude': start_alt,
            'end_altitude': end_alt,
            'rvsm_interval': interval,
            'unit': unit
        })
    
    return altitude_ranges

# Example usage
altitude_data = parse_altitude_restrictions("M0090M0060M0810")
print(f"Altitude range: {altitude_data[0]['start_altitude']}-{altitude_data[0]['end_altitude']} meters")
print(f"RVSM interval: {altitude_data[0]['rvsm_interval']} meters")
```

### Altitude Layer Examples

```python
def decode_altitude_examples():
    """Decode altitude layer examples."""
    examples = {
        'M0090M0060M0810': {
            'description': 'Metric units, 900-8100 meters, RVSM interval 600 meters',
            'start': 900,
            'end': 8100,
            'interval': 600,
            'unit': 'meters'
        },
        '010000200027000': {
            'description': 'Feet units, 10000-27000 feet, RVSM interval 2000 feet',
            'start': 10000,
            'end': 27000,
            'interval': 2000,
            'unit': 'feet'
        },
        'UNLTD': {
            'description': 'Unlimited altitude',
            'start': None,
            'end': None,
            'interval': None,
            'unit': None
        }
    }
    return examples
```

## Sector Analysis

### Regional Grouping

```python
from collections import defaultdict

def analyze_sectors_by_region(sector_lines):
    """Analyze sector data by region."""
    sectors = defaultdict(list)
    
    for line in sector_lines:
        if len(line.strip()) > 0:
            # Extract first two characters as region code
            region_code = line[:2].strip()
            sectors[region_code].append(line.strip())
    
    # Count sectors per region
    region_stats = {}
    for region, sector_list in sectors.items():
        region_stats[region] = {
            'sector_count': len(sector_list),
            'has_true_heading': any('T' in sector for sector in sector_list),
            'has_magnetic_heading': any('M' in sector for sector in sector_list),
            'altitude_restricted': any('UNLTD' not in sector for sector in sector_list)
        }
    
    return region_stats

# Example usage
stats = analyze_sectors_by_region(sector_lines)
for region, data in stats.items():
    print(f"Region {region}: {data['sector_count']} sectors")
```

### Heading Coverage Analysis

```python
def analyze_heading_coverage(sector_data):
    """Analyze heading coverage."""
    heading_coverage = {}
    
    for sector in sector_data:
        parts = sector.split()
        if len(parts) >= 3:
            region = parts[0][:2]
            start_heading = int(parts[0][2:5])
            end_heading = int(parts[1])
            
            if region not in heading_coverage:
                heading_coverage[region] = []
            
            heading_coverage[region].append({
                'start': start_heading,
                'end': end_heading,
                'range': calculate_heading_range(start_heading, end_heading)
            })
    
    return heading_coverage

def calculate_heading_range(start, end):
    """Calculate heading range in degrees."""
    if start <= end:
        return end - start + 1
    else:
        return (360 - start) + end + 1
```

## Altitude Optimization

### Optimal Altitude Selection

```python
def find_optimal_altitude(sector_data, aircraft_performance):
    """Find optimal altitude based on sector restrictions."""
    optimal_altitudes = {}
    
    for sector in sector_data:
        # Parse sector altitude restrictions
        altitude_restrictions = parse_sector_altitudes(sector)
        
        # Find performance optimal altitude layer
        for restriction in altitude_restrictions:
            if restriction['unit'] == 'feet':
                # Convert to standard flight levels
                fl_start = restriction['start'] // 100
                fl_end = restriction['end'] // 100
                
                # Find optimal FL within allowed range
                optimal_fl = find_best_flight_level(
                    fl_start, fl_end, aircraft_performance
                )
                
                optimal_altitudes[sector[:2]] = {
                    'optimal_fl': optimal_fl,
                    'altitude_feet': optimal_fl * 100,
                    'restriction_range': f"FL{fl_start}-FL{fl_end}"
                }
    
    return optimal_altitudes
```

## Data Validation

### Sector Integrity Check

```python
def validate_sector_data(sector_lines):
    """Validate sector data integrity."""
    issues = []
    region_coverage = defaultdict(list)
    
    for line in sector_lines:
        if len(line.strip()) > 0:
            parts = line.split()
            if len(parts) >= 3:
                region = parts[0][:2]
                start_heading = int(parts[0][2:5])
                end_heading = int(parts[1])
                
                region_coverage[region].append((start_heading, end_heading))
    
    # Check if each region has complete heading coverage
    for region, headings in region_coverage.items():
        total_coverage = 0
        for start, end in headings:
            total_coverage += calculate_heading_range(start, end)
        
        if total_coverage < 360:
            issues.append(f"Region {region} heading coverage incomplete: {total_coverage}°/360°")
        elif total_coverage > 360:
            issues.append(f"Region {region} heading coverage overlaps: {total_coverage}°/360°")
    
    return issues
```

## Data Integration

Cruise sector data connects to other navdata sections:

- **[Airways](./airways.md)**: Airway restrictions within sectors
- **[Waypoints](./waypoints.md)**: Navigation points at sector boundaries
- **[SID Procedures](./sid-procedures.md)**: Sector control during departure
- **[STAR Procedures](./star-procedures.md)**: Sector control during arrival

## Practical Applications

### Flight Plan Integration

```python
def integrate_with_flight_plan(route_waypoints, sector_data):
    """Integrate sector data with flight plan."""
    sector_assignments = []
    
    for i, waypoint in enumerate(route_waypoints):
        # Calculate segment track
        if i < len(route_waypoints) - 1:
            next_waypoint = route_waypoints[i + 1]
            track = calculate_track(waypoint, next_waypoint)
            
            # Find applicable sector
            applicable_sector = find_sector_for_track(track, sector_data)
            
            sector_assignments.append({
                'waypoint': waypoint['name'],
                'track': track,
                'sector': applicable_sector,
                'altitude_restrictions': parse_sector_altitudes(applicable_sector)
            })
    
    return sector_assignments
```

## Next Steps

- **[Learn about airspace management](./airways.md)** - Sector and airway relationships
- **[Explore navigation methods](./waypoints.md)** - Sector boundary navigation
- **[Use flight planning tools](../tools/examples.md)** - Applying sector data in flight planning
