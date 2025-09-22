# SID Procedures (Standard Instrument Departures)

Standard Instrument Departure (SID) procedures provide standardized routing from airports to the enroute structure. Each SID consists of multiple waypoints that define the departure path.

## Format Structure

```
SID ICAORRR  DDDDDDWWWWWWNNNNNPPPPPPTTTTTTT ±LLLLLLLLL±LLLLLLLLLR
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
