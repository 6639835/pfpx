# File Header

The PFPX navdata file header contains essential metadata about the navigation database in plaintext format.

## Structure

The header appears at the beginning of every navdata file and is **not encoded**. It provides information about the data source, version, and validity period.

## Format Example

```
PFPX NAVDATA
NG2509
2025/09/04
2025/10/01
NAVIGRAPH
```

## Field Descriptions

### Line 1: Database Identifier
```
PFPX NAVDATA
```
- **Purpose**: Identifies the file as PFPX navigation data
- **Format**: Fixed string
- **Required**: Yes

### Line 2: Database Version
```
NG2509
```
- **Purpose**: Database version/cycle identifier
- **Format**: Provider prefix + cycle number
- **Examples**:
  - `NG2509` = Navigraph cycle 2509
  - `AS2509` = Aerosoft cycle 2509

### Line 3: Effective Date
```
2025/09/04
```
- **Purpose**: When the navigation data becomes valid
- **Format**: `YYYY/MM/DD`
- **Standard**: Follows AIRAC cycle dates

### Line 4: Expiration Date
```
2025/10/01
```
- **Purpose**: When the navigation data expires
- **Format**: `YYYY/MM/DD`
- **Standard**: Follows AIRAC cycle dates (28-day intervals)

### Line 5: Data Provider
```
NAVIGRAPH
```
- **Purpose**: Identifies the navigation data source
- **Common Values**:
  - `NAVIGRAPH` - Navigraph navigation data
  - `AEROSOFT` - Aerosoft navigation data
  - Custom provider names may appear

## AIRAC Cycles

Navigation data follows the AIRAC (Aeronautical Information Regulation and Control) standard:

- **Cycle Length**: 28 days
- **Global Standard**: Ensures worldwide consistency
- **Updates**: Regular updates to reflect changes in airways, procedures, etc.

### Cycle Numbering

AIRAC cycles are numbered sequentially:
- **Format**: YYWW (Year + Week number)
- **Example**: `2509` = 2025, cycle 9

## Validation

When processing navdata files, always verify:

1. **Date Validity**: Check if current date is within effective period
2. **Version Matching**: Ensure compatibility with your PFPX version
3. **Provider Consistency**: Confirm expected data source

## Programming Notes

### Parsing Example (Python)

```python
def parse_header(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [f.readline().strip() for _ in range(5)]
    
    return {
        'database': lines[0],
        'version': lines[1],
        'effective_date': lines[2],
        'expiration_date': lines[3],
        'provider': lines[4]
    }
```

### Date Handling

```python
from datetime import datetime

def is_current(effective_date, expiration_date):
    today = datetime.now().date()
    effective = datetime.strptime(effective_date, '%Y/%m/%d').date()
    expiration = datetime.strptime(expiration_date, '%Y/%m/%d').date()
    
    return effective <= today <= expiration
```

## Common Issues

### Encoding Problems
- **Symptom**: Garbled header text
- **Cause**: Wrong text encoding
- **Solution**: Use UTF-8 or ANSI encoding

### Date Format Variations
- **Standard**: `YYYY/MM/DD`
- **Alternatives**: Some files may use different separators
- **Handling**: Implement flexible date parsing

### Missing Lines
- **Issue**: Truncated headers
- **Cause**: File corruption or incomplete downloads
- **Detection**: Check for exactly 5 header lines

## Integration

The header information is crucial for:

- **Version Control**: Tracking database updates
- **Validation**: Ensuring data currency
- **Compatibility**: Matching with PFPX versions
- **Logging**: Recording data sources and versions

## Next Steps

- **[Learn about runway data](./runways.md)** - First encoded section
- **[Understand the overall structure](./file-structure.md)** - How sections relate
- **[Use decoding tools](../tools/)** - Process the encoded content
