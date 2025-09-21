# Waypoints and Navigation Facilities

The waypoint section contains various types of navigation points including airports, navigation aids, and route waypoints.

## Waypoint Types

Each waypoint has a type code that identifies its category:

| Type | Description | Usage |
|------|-------------|-------|
| 0 | Airport | Terminal facilities |
| 1 | VFR Waypoint | Visual reference points |
| 2 | VOR/TACAN | Combined navigation aid |
| 3 | TACAN | Military tactical navigation |
| 4 | VOR/DME | VOR with distance measuring |
| 5 | NDB | Non-directional beacon |
| 6 | Route Waypoint | Intersection/fix |
| 9 | DME | Distance measuring equipment |

## Airport Records (Type 0)

Airports represent terminal facilities with runways and services.

### Format
```
WPT ICAO IATA0ICAOAREA1CAREAGIONNAMEEEEE        DDDDDD     ±LLLLLLLLL±LLLLLLLLL±EEEEERRRRRFIRCODE    TTTT
```

### Example
```
WPT ZBAA PEK0ZBAAZBP 1CZBCAPITAL                       016256     +40073333+116598333+0011612467ZBPE    9850
```

### Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `WPT` | Waypoint type identifier | Fixed value indicating this record is a waypoint/airport/navigation facility |
| `ZBAA` | ICAO code |  |
| `PEK` | IATA code |  |
| `0` | Type code | 0 = Airport |
| `ZBAA` | ICAO code | Same as ICAO above |
| `ZB` | Region code |  |
| `P` | Section code | Airport (ref ARINC424-18 5.4) |
| `1` | Flag | Fixed value indicating this record is an airport |
| `C` | Airport category | C = Civil, M = Military, P = Private |
| `ZB` | Region code |  |
| `CAPITAL` | Name |  |
| `016256` | Database ID | Unique identifier |
| `+40073333` | Latitude | WGS-84, decimal degrees × 1e6, + = North, - = South → 40.073333°N |
| `+116598333` | Longitude | WGS-84, decimal degrees × 1e6, + = East, - = West → 116.598333°E |
| `+00116` | Elevation (feet) | + = Above MSL, - = Below MSL |
| `12467` | Longest runway length (feet) | e.g., 12,467 ft |
| `ZBPE` | Airport FIR code |  |
| `9850` | Transition altitude (ft) |  |

## Route Waypoints (Type 6)

Intersections and fixes used for navigation routing.

### Example  
```
WPT AVBOX   6AVBOXZBE0 ZBAVBOX                         097808     +38647778+116378056+0000000000ZBPE   
```

### Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `WPT` | Waypoint type identifier | Fixed value indicating this record is a waypoint/airport/navigation facility |
| `AVBOX` | Waypoint identifier |  |
| `6` | Type code | 6 = Waypoint |
| `AVBOX` | Waypoint identifier |  |
| `ZB` | Region code |  |
| `E` | Section code | E = Enroute, P = Airport (ref ARINC424-18 5.4) |
| `0` | Terminal area flag | 0 = Not terminal area waypoint, 1 = Terminal area waypoint |
| `ZB` | Region code |  |
| `AVBOX` | Waypoint name | If named by VOR bearing and distance, would be `ZUH345015` |
| `097808` | Database ID |  |
| `+38647778` | Latitude |  |
| `+116378056` | Longitude |  |
| `+0000000000` | Unused field | Waypoint does not need this field |
| `ZBPE` | Flight Information Region |  |

## VOR Stations (Type 4)

VOR navigation aids.

### Example
```
WPT PEK     4PEKZBD  0 ZBGUANZHUANG                    27126111470+40048333+116735000+0020300000ZBPE
```

### Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `WPT` | Waypoint type identifier | Fixed value indicating this record is a waypoint/airport/navigation facility |
| `PEK` | VOR identifier |  |
| `4` | Type code | 4 = VOR/DME |
| `PEK` | VOR identifier |  |
| `ZB` | Region code |  |
| `D` | Section code | D = Navigation facility (ref ARINC424-18 5.4) |
| `0` | Terminal area flag | 0 = Not terminal area waypoint, 1 = Terminal area waypoint |
| `ZB` | Region code |  |
| `GUANZHUANG` | Name |  |
| `271261` | Database ID |  |
| `11470` | Frequency | 11470 = 114.70 MHz |
| `+40048333` | Latitude |  |
| `+116735000` | Longitude |  |
| `+00203` | Elevation | Elevation (feet), + = Above MSL, - = Below MSL |
| `00000` | Unused field | VOR does not need this field |
| `ZBPE` | Flight Information Region |  |

## NDB Stations (Type 5)

Non-Directional Beacon radio navigation aids.

### Example
```
WPT CU      5CUZBD   0 ZBSHAHE                         27392005550+40121667+116371667+0000000000ZBPE 
```

### Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `WPT` | Waypoint type identifier | Fixed value indicating this record is a waypoint/airport/navigation facility |
| `CU` | NDB identifier |  |
| `5` | Type code | 5 = NDB |
| `CU` | NDB identifier |  |
| `ZB` | Region code |  |
| `D` | Section code | D = Navigation facility (ref ARINC424-18 5.4) |
| `0` | Terminal area flag | 0 = Not terminal area waypoint, 1 = Terminal area waypoint |
| `ZB` | Region code |  |
| `SHAHE` | Name |  |
| `273920` | Database ID |  |
| `05550` | Frequency | 05550 = 555.0 kHz |
| `+40121667` | Latitude |  |
| `+116371667` | Longitude |  |
| `0000000000` | Unused field | NDB does not use this field |
| `ZBPE` | Flight Information Region |  |

## Coordinate Conversion

All waypoint coordinates use the same format:

### Latitude
```
±DDDDDDDD (degrees × 1,000,000)
+40073333 → 40.073333°N
-40073333 → 40.073333°S
```

### Longitude  
```
±DDDDDDDDD (degrees × 1,000,000)  
+116598333 → 116.598333°E
-116598333 → 116.598333°W
```

## Related Data

Waypoints connect to other navdata sections:

- **[Airways](./airways.md)**: Routes connect waypoints
- **[SID Procedures](./sid-procedures.md)**: Reference specific waypoints
- **[STAR Procedures](./star-procedures.md)**: Use waypoints for routing

## Next Steps

- **[Learn about airways](./airways.md)** - How waypoints connect via routes
- **[Explore procedures](./sid-procedures.md)** - Waypoint usage in SID/STAR
- **[Use analysis tools](../tools/examples.md)** - Extract and analyze waypoint data
