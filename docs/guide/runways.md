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

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `RWY` | Record type identifier | Fixed string "RWY" identifying this as runway data |
| `ZBAA` | ICAO airport code | 4-character ICAO identifier (e.g., `ZBAA` = Beijing Capital International Airport) |
| `01` | Runway number | 2-digit runway designation (01-36), based on magnetic heading rounded to nearest 10° |
| `12467` | Runway length | Physical runway length in feet (e.g., `12467` = 12,467 feet) |
| `197` | Runway width | Physical runway width in feet (e.g., `197` = 197 feet) |
| `359` | Magnetic heading | 3-digit runway magnetic bearing (000-359°) |
| `ASP` | Surface type | Runway surface material, always "ASP" (Asphalt) in PFPX data |
| `+40058914` | Threshold latitude | Runway threshold latitude coordinate ±DDDDDDDD (degrees × 1,000,000), + = North, - = South |
| `+116617658` | Threshold longitude | Runway threshold longitude coordinate ±DDDDDDDDD (degrees × 1,000,000), + = East, - = West |

## Coordinate Conversion

### Latitude Example
```
+40058914 → 40058914 ÷ 1,000,000 = 40.058914°N
```

### Longitude Example
```
+116617658 → 116617658 ÷ 1,000,000 = 116.617658°E
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
