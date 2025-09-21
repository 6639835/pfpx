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

RWY 00AN03   04517060030ASP+59088889-156463889
RWY 00AN21   04517060210ASP+59098056-156447778
......
RWY ZYYJ09   08530148092ASP+42881175+129435625
RWY ZYYJ27   08530148272ASP+42884531+129467125

WPT ENOE QAT0ENOEA1P 1CA1TROLL AIRFIELD                003733     -71956667+002453333+0412509843ENOR    18000
WPT NZFX    0NZFXA1P 1PA1PHOENIX                       011402     -77957092+166745389+0003710006NZZO    18000
......
WPT ZYTX SHE0ZYTXZYP 1CZYTAOXIAN                       016367     +41641667+123485000+0019810499ZYSH    
WPT ZYYJ YNJ0ZYYJZYP 1CZYCHAOYANGCHUAN                 016368     +42881667+129450000+0062208530ZYSH    9490

WPT AARON   6AARONA1E0 A1AARON                         016368     -79384500-110927167+0000000000NZZO         
WPT ANGIE   6ANGIEA1E0 A1ANGIE                         016369     -89754667-176959167+0000000000NZZO       
......
WPT LJ      5LJZYP   0 ZYSANJIAZI QIQIHAR              27493901770+47195903+123944392+0000000000ZYSH         
WPT JA      5JAZYP   0 ZYDEXIN YANJI                   27494003320+42871356+129341022+0000000000ZYSH            

AWY A1    SA32690940745071+33447742+135794494+33364503+13544151408000UNLTD0
AWY A1    SA30745070749101+33364503+135441514+33248769+13499722208000UNLTD0
......
AWY Z999  SO30223222639891+47559389+010305583+47745775+01034983309500FL6601
AWY Z999  SA22639890222801+47745775+010349833+47929603+01074995606500FL2451

SID 0ID211   000001099539FLNGJYOYYU1      +44255928-1134392501
SID 0ID211   000002034960YOYYUYOYYU1      +43948250-1133553641
......
SID ZYYJ27   164665263457YJ401WQG19D      +43242778+1297413891
SID ZYYJ27   164666271707WQG  WQG19D      +43293333+1297850001

STR 06FAALL  164667050581BISKSCLMNT2BISKS +27981592-0796214061
STR 06FAALL  164668051894HEMSICLMNT2BISKS +27640356-0797136671
......
STR ZYYJ27   330409263457YJ401WQG19A      +43242778+1297413891
STR ZYYJ27   330410263468YJ604WQG19A      +43017778+1296950001
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

## Next Steps

- **[Explore data sections](./runways.md)** - Learn about specific data formats
- **[Use Python tools](../tools/python-decoder.md)** - Automate the process
- **[See examples](../tools/examples.md)** - Practical usage scenarios
