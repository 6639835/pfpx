# Runway Data

The runway section contains detailed information about airport runways worldwide, including dimensions, orientation, and geographic coordinates.

## Format Structure

Each runway record follows this pattern:

```
RWY ICAO## LLLLWWWHHHASP±LLLLLLLLL±LLLLLLLLL
```

## Example Record

```
RWY ZBAA01   12467197359ASP+40058914+116617658
```

## Field Breakdown

### Record Type
```
RWY
```
- **Purpose**: Identifies this as runway data
- **Format**: Fixed string "RWY"
- **Required**: Yes

### Airport Code
```
ZBAA
```
- **Purpose**: ICAO airport identifier
- **Format**: 4-character ICAO code
- **Example**: `ZBAA` = Beijing Capital International Airport

### Runway Number
```
01
```
- **Purpose**: Runway designation
- **Format**: 2-digit runway number (01-36)
- **Magnetic**: Based on magnetic heading rounded to nearest 10°
- **Examples**:
  - `01` = Runway 01
  - `36` = Runway 36
  - `09` = Runway 09

### Runway Length
```
12467
```
- **Purpose**: Physical runway length
- **Format**: Length in feet
- **Example**: `12467` = 12,467 feet

### Runway Width  
```
197
```
- **Purpose**: Physical runway width
- **Format**: Width in feet
- **Example**: `197` = 197 feet

### Magnetic Heading
```
359
```
- **Purpose**: Runway magnetic bearing
- **Format**: 3-digit heading (000-359)
- **Example**: `359` = 359° magnetic

### Surface Type
```
ASP
```
- **Purpose**: Runway surface material
- **Format**: Fixed value "ASP" (Asphalt)
- **Note**: Always appears as "ASP" in PFPX data

### Threshold Latitude
```
+40058914
```
- **Purpose**: Runway threshold latitude coordinate
- **Format**: ±DDDDDDDD (degrees × 1,000,000)
- **Sign**: `+` = North, `-` = South
- **Conversion**: Divide by 1,000,000 to get decimal degrees

### Threshold Longitude
```
+116617658
```
- **Purpose**: Runway threshold longitude coordinate  
- **Format**: ±DDDDDDDDD (degrees × 1,000,000)
- **Sign**: `+` = East, `-` = West
- **Conversion**: Divide by 1,000,000 to get decimal degrees

## Coordinate Conversion

### Latitude Example
```
+40058914 → 40058914 ÷ 1,000,000 = 40.058914°N
```

### Longitude Example
```
+116617658 → 116617658 ÷ 1,000,000 = 116.617658°E
```

## Programming Examples

### Python Parsing

```python
import re

def parse_runway(line):
    pattern = r'RWY (\w{4})(\d{2})\s+(\d+)(\d{3})(\d{3})ASP([+-]\d{8})([+-]\d{9})'
    match = re.match(pattern, line)
    
    if match:
        return {
            'icao': match.group(1),
            'runway': match.group(2),
            'length_ft': int(match.group(3)),
            'width_ft': int(match.group(4)),
            'heading': int(match.group(5)),
            'latitude': int(match.group(6)) / 1_000_000,
            'longitude': int(match.group(7)) / 1_000_000
        }
    return None
```

### Coordinate Conversion

```python
def convert_coordinates(lat_raw, lon_raw):
    """Convert raw coordinate values to decimal degrees"""
    latitude = int(lat_raw) / 1_000_000
    longitude = int(lon_raw) / 1_000_000
    
    lat_hemisphere = 'N' if latitude >= 0 else 'S'
    lon_hemisphere = 'E' if longitude >= 0 else 'W'
    
    return {
        'latitude': abs(latitude),
        'longitude': abs(longitude),
        'lat_hemisphere': lat_hemisphere,
        'lon_hemisphere': lon_hemisphere
    }
```

## Data Validation

### Common Checks

1. **Length Range**: Runway length should be reasonable (500-20,000 ft)
2. **Width Range**: Runway width typically 75-400 ft
3. **Heading Range**: Must be 000-359°
4. **Coordinate Range**: 
   - Latitude: -90° to +90°
   - Longitude: -180° to +180°

### Example Validation

```python
def validate_runway(runway_data):
    errors = []
    
    if not (500 <= runway_data['length_ft'] <= 20000):
        errors.append("Invalid runway length")
    
    if not (75 <= runway_data['width_ft'] <= 400):
        errors.append("Invalid runway width")
    
    if not (0 <= runway_data['heading'] <= 359):
        errors.append("Invalid heading")
    
    return errors
```

## Related Data

Runway data connects to other navdata sections:

- **[Waypoints](./waypoints.md)**: Airport waypoints reference runways
- **[SID Procedures](./sid-procedures.md)**: Departures specify runway
- **[STAR Procedures](./star-procedures.md)**: Arrivals specify runway

## Next Steps

- **[Learn about waypoint data](./waypoints.md)** - Navigation points and facilities
- **[Explore airport waypoints](./waypoints.md#airports)** - Related airport information
- **[Use decoding tools](../tools/)** - Extract and analyze runway data
