# File Structure

PFPX navdata files follow a well-defined structure with distinct sections for different types of navigation data.

## Overall Organization

A typical navdata file is organized as follows:

```
┌─────────────────┐
│   File Header   │ ← Plaintext metadata
│   (Plaintext)   │
├─────────────────┤
│                 │
│   Runway Data   │ ← Encoded content begins
│     (RWY)       │
│                 │
├─────────────────┤
│                 │
│  Waypoint Data  │ ← Airports, VOR, NDB, etc.
│     (WPT)       │
│                 │
├─────────────────┤
│                 │
│  Airway Data    │ ← Route information
│     (AWY)       │
│                 │
├─────────────────┤
│                 │
│   SID Data      │ ← Departure procedures
│     (SID)       │
│                 │
├─────────────────┤
│                 │
│   STAR Data     │ ← Arrival procedures
│     (STR)       │
│                 │
└─────────────────┘
```

## Section Details

### File Header (Plaintext)
The header contains metadata about the navigation database:
- Database name and version
- Effective dates (AIRAC cycle)
- Data provider information

### Runway Section (RWY)
Contains runway information for airports worldwide:
- Runway dimensions and orientation
- Surface type and condition
- Geographic coordinates

### Waypoint Section (WPT)
Includes all types of navigation points:
- **Airports** (Type 0)
- **VFR Waypoints** (Type 1)  
- **VOR/TACAN** (Type 2)
- **TACAN** (Type 3)
- **VOR/DME** (Type 4)
- **NDB** (Type 5)
- **Route Waypoints** (Type 6)
- **DME** (Type 9)

### Airway Section (AWY)
Defines airways and routes:
- High altitude airways
- Low altitude airways  
- RNAV routes
- Route segments with waypoint connections

### SID Section (SID)
Standard Instrument Departure procedures:
- Departure routes from airports
- Transition procedures
- Runway-specific departures

### STAR Section (STR)
Standard Terminal Arrival Route procedures:
- Arrival routes to airports
- Approach transitions
- Runway-specific arrivals

## Data Encoding

### Header vs Content
- **Header**: Stored in plaintext ASCII
- **Content**: Encoded using XOR encryption with key `0x85`

### Line-by-Line Format
Each encoded section follows a line-by-line format where:
- Each line represents one data record
- Lines are separated by standard newline characters
- Record format varies by section type

## Record Identification

Each record type can be identified by its prefix:

| Prefix | Section | Description |
|--------|---------|-------------|
| `RWY` | Runway | Runway information |
| `WPT` | Waypoint | Navigation points |
| `AWY` | Airway | Route segments |
| `SID` | Departure | Standard departures |
| `STR` | Arrival | Standard arrivals |

## File Size Considerations

Navdata files can be quite large:
- **Typical size**: 50-200 MB
- **Record count**: Hundreds of thousands of records
- **Global coverage**: Worldwide navigation data

## Processing Notes

::: tip Batch Processing
Due to file size, consider processing in chunks:
- Process 3,000-4,000 lines at a time when using manual tools
- Use streaming for automated processing
- Implement progress tracking for large operations
:::

## Next Steps

- **[Learn about decoding](./decoding-process.md)** - Convert encoded data to readable format
- **[Explore specific sections](./runways.md)** - Detailed format for each data type
- **[Use automation tools](../tools/)** - Handle large files efficiently
