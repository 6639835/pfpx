# Decoding Process

This guide explains how to convert encoded PFPX navdata files into readable text format.

## Overview

PFPX navdata files use XOR encryption with a custom character mapping. The decoding process reverses this encryption to reveal the original navigation data.

## Manual Decoding Method

### Requirements
- **Notepad++** with Converter plugin
- PFPX navdata file (`.nav`)
- Time and patience (for large files)

### Step-by-Step Process

1. **Open the file in Notepad**
   ```
   File → Open → navdata.nav
   ```
   You'll see the plaintext header followed by encoded content.

2. **Switch to Notepad++**
   - Open the same file in Notepad++
   - You'll see the same header + encoded sections

3. **Select the encoded content**
   - Start from line 9 (skip the plaintext header)
   - Select the content you want to decode
   - **Important**: Don't select more than 3,000-4,000 lines at once

4. **Convert to hexadecimal**
   ```
   Menu → Plugins → Converter → ASCII-to-HEX
   ```

5. **Apply character mapping**
   - Use the [encoding table](./encoding-table.md) to convert hex codes
   - Each pair of hex characters represents one original character

### Important Notes

::: warning File Handling
- **Never modify the original file directly**
- **Always work on a copy**
- **Use ANSI encoding** when saving new files
- **Process in small chunks** to avoid errors
:::

## Automated Decoding Method

Our Python decoder automates this entire process:

### Basic Usage

```bash
# Decode a navdata file
python nav_decoder.py decode navdata.nav output.txt

# Encode a text file back to navdata format  
python nav_decoder.py encode input.txt navdata.nav
```

### Auto-processing Mode

```bash
# Automatically process files with standard names
python nav_decoder.py auto
```

This looks for:
- `wait2decode.nav` → creates `already_decode.txt`
- `wait2encode.txt` → creates `already_encode.nav`

## Understanding the Output

Once decoded, you'll see readable navigation data:

```txt
PFPX NAVDATA
NG2509
2025/09/04
2025/10/01
NAVIGRAPH

RWY ZBAA01   12467197359ASP+40058914+116617658
RWY ZBAA19   12467197179ASP+40073556+116598889
...

WPT ZBAA PEK0ZBAAZBP 1CZBCAPITAL                       016256     +40073333+116598333+0011612467ZBPE    9850
WPT AVBOX   6AVBOXZBE0 ZBAVBOX                         097808     +38647778+116378056+0000000000ZBPE   
...
```

## Validation

After decoding, verify your results:

1. **Check the header** - Should be identical to original
2. **Verify record formats** - Each line should follow expected patterns
3. **Count records** - Compare with expected quantities
4. **Test encoding** - Re-encode and compare with original

## Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Converter plugin missing | Notepad++ installation | Install Converter plugin |
| "Error" message | Processing too many lines | Reduce selection size |
| Garbled output | Wrong encoding | Use ANSI encoding |
| Missing characters | Incomplete selection | Include full line ranges |

### Performance Tips

- **Chunk processing**: Process 3,000-4,000 lines at a time
- **Progress tracking**: Use automated tools for large files
- **Memory management**: Close other applications for large operations
- **Backup strategy**: Always keep original files safe

## Integration Options

### Scripting
```python
from nav_codec import NavCodec

codec = NavCodec()
codec.decode_file("navdata.nav", "output.txt")
```

### Batch Processing
```bash
# Process multiple files
for file in *.nav; do
    python nav_decoder.py decode "$file" "${file%.nav}.txt"
done
```

### Custom Applications
The decoder can be integrated into larger applications for:
- Flight planning tools
- Navigation database analysis
- Data validation and verification
- Format conversion utilities

## Next Steps

- **[Explore data sections](./runways.md)** - Learn about specific data formats
- **[Use Python tools](../tools/python-decoder.md)** - Automate the process
- **[See examples](../tools/examples.md)** - Practical usage scenarios
