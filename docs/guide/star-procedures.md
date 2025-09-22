# STAR Procedures (Standard Terminal Arrival Routes)

Standard Terminal Arrival Route (STAR) procedures provide structured routing from the enroute environment to the airport terminal area. Each STAR consists of waypoints defining the arrival path.

## Format Structure

```
STR ICAORRR  DDDDDDWWWWWWNNNNNPPPPPPTTTTTTT ±LLLLLLLLL±LLLLLLLLLR
```

## Example Records

```
STR YWLMALL  319972094283EKIPUIVTA1REKIPU -33207250+1517406671
STR YWLM30   319979258061UBGIMIVTA1R      -32942194+1518618331
STR YWLM30   319980263047IVTA1RIVTA1R      -33109636+1514653191
STR YWLM30   319981258062DOMBLIVTA1R      -33143681+1515064721
```

## Field Breakdown

| Field | Meaning | Notes / Examples |
|-------|---------|------------------|
| `STR` | Arrival procedure identifier | Fixed value indicating this record is a STAR |
| `YWLM` | ICAO code |  |
| `ALL` | Runway designation | ALL = All runways; xxB = xxL / xxC / xxR |
| `319972` | STAR procedure database ID |  |
| `094283` | Waypoint ID (current line) |  |
| `EKIPU` | Waypoint name (current line) |  |
| `IVTA1R` | Procedure identifier |  |
| `EKIPU` | Procedure transition point | If transition point exists, its name is filled in |
| `-33207250` | Latitude (current waypoint) |  |
| `+151740667` | Longitude (current waypoint) |  |
| `1` | RNAV procedure flag | 0 = No, 1 = Yes |

## Runway Designations

### Standard Format
- **Specific Runway**: `30`, `36`, `27L` - Applies to single runway
- **All Runways**: `ALL` - Applies to all runways  
- **Grouped Runways**: `36B` - Applies to 36L/36C/36R

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
