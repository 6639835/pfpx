# Getting Started

This guide will help you understand and work with PFPX navigation data files.

## Prerequisites

Before you begin, you'll need:

- Basic understanding of aviation navigation concepts
- A text editor (Notepad++ recommended for manual decoding)
- Python 3.6+ (if using our decoder tools)
- PFPX navdata files (`.nav` extension)

## Understanding Navdata Files

PFPX navdata files contain encoded navigation data that needs to be decoded before it can be read or modified.

### File Location

Navdata files are typically found in your PFPX installation directory:
```
PFPX Installation Folder/
├── Data/
│   └── navdata.nav
└── ...
```

### File Structure Overview

Each navdata file consists of:

1. **Header Section** (plaintext) - Contains metadata
2. **Encoded Content** - Navigation data using custom encoding

## Quick Example

Here's what you'll see when opening a navdata file:

```
PFPX NAVDATA
NG2509
2025/09/04
2025/10/01
NAVIGRAPH

[Encoded binary data follows...]
```

The first few lines are readable, but the navigation data below is encoded and appears as gibberish in a regular text editor.

## Next Steps

1. **[Learn about the file structure](./file-structure.md)** - Understand how the file is organized
2. **[Study the encoding table](./encoding-table.md)** - Learn the character mapping system
3. **[Try the decoding process](./decoding-process.md)** - Convert encoded files to readable text
4. **[Use our tools](../tools/)** - Automate the process with Python scripts

## Manual vs Automated Decoding

### Manual Method
- Use Notepad++ with Converter plugin
- Good for learning and small files
- Time-consuming for large datasets

### Automated Method
- Use our Python decoder tools
- Fast and reliable
- Better for batch processing and integration

Choose the method that best fits your needs and technical comfort level.
