# Airways and Routes

Airways define the route structure connecting waypoints for aircraft navigation. They specify altitude constraints, routing, and operational parameters.

> **📍 Looking for cruise tables?** See **[Cruise Tables](./cruise-table.md)** for global airway RVSM information.

## Format Structure

```
AWY ROUTE  AA#SSSSSSEEEEEED±LLLLLLLLL±LLLLLLLLLL±LLLLLLLLL±LLLLLLLLLLAAAAAUUUUUR
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

## Data Integration

Airways connect to other navdata sections:

- **[Waypoints](./waypoints.md)**: Start/end points of route segments
- **[SID Procedures](./sid-procedures.md)**: Connect to airway system
- **[STAR Procedures](./star-procedures.md)**: Connect from airway system

## Next Steps

- **[Learn about SID procedures](./sid-procedures.md)** - How departures connect to airways
- **[Explore STAR procedures](./star-procedures.md)** - How arrivals use airways
- **[Use analysis tools](../tools/examples.md)** - Extract and analyze airway data