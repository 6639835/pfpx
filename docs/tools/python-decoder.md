# Python Decoder

A comprehensive Python tool for encoding and decoding PFPX navdata files with advanced features and automation capabilities.

## Installation

### Requirements
- **Python 3.6+**
- No additional dependencies required (uses only standard library)

### Setup
1. Download the decoder from the `tools/` directory
2. Make it executable (Unix/Linux):
   ```bash
   chmod +x nav_decoder.py
   ```

## Basic Usage

### Command Line Interface

```bash
# Decode a navdata file
python nav_decoder.py decode input.nav output.txt

# Encode a text file back to navdata format
python nav_decoder.py encode input.txt output.nav

# Auto-process files with standard names
python nav_decoder.py auto
```

### Auto-Processing Mode

The auto mode looks for these files in the current directory:

| Input File | Output File | Operation |
|------------|-------------|-----------|
| `wait2decode.nav` | `already_decode.txt` | Decode |
| `wait2encode.txt` | `already_encode.nav` | Encode |

## Advanced Options

### Custom XOR Key
```bash
# Use a different XOR key (default is 0x85)
python nav_decoder.py -k 0xFF decode input.nav output.txt

# Hexadecimal format
python nav_decoder.py --xor-key 0x90 decode input.nav output.txt
```

### Working Directory
```bash
# Process files in a different directory
python nav_decoder.py -d /path/to/files auto
```

### Verbose Output
```bash
# Enable detailed logging
python nav_decoder.py -v decode input.nav output.txt
```

### Progress Steps
```bash
# Control progress reporting frequency
python nav_decoder.py --steps 50 decode large_file.nav output.txt
```

## Python API

### Basic Usage

```python
from pathlib import Path
from tools.nav_decoder import NavCodec

# Create codec instance
codec = NavCodec()

# Decode a file
codec.decode_file(Path("navdata.nav"), Path("decoded.txt"))

# Encode a file
codec.encode_file(Path("input.txt"), Path("encoded.nav"))
```

### Custom Configuration

```python
from tools.nav_decoder import NavCodec, CodecConfig

# Custom configuration
config = CodecConfig(
    xor_key=0xFF,           # Different XOR key
    progress_steps=50,      # More progress updates
    encoding='utf-8'        # Text encoding
)

codec = NavCodec(config)
```

### Error Handling

```python
from tools.nav_decoder import NavCodec, NavCodecError

try:
    codec = NavCodec()
    codec.decode_file(Path("input.nav"), Path("output.txt"))
    print("Decode successful!")
except NavCodecError as e:
    print(f"Codec error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Configuration Options

The `CodecConfig` class provides these settings:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `xor_key` | `0x85` | XOR key for encoding/decoding |
| `header_threshold` | `128` | Byte threshold for header detection |
| `content_line_threshold` | `30` | Line length threshold for content detection |
| `progress_steps` | `20` | Number of progress updates |
| `encoding` | `utf-8` | Text file encoding |

## Performance Features

### Progress Tracking
```
2025-01-15 10:30:15 - INFO - Starting decode operation: navdata.nav -> output.txt
2025-01-15 10:30:20 - INFO - Progress: 5%
2025-01-15 10:30:25 - INFO - Progress: 10%
...
2025-01-15 10:32:45 - INFO - Decode completed successfully. Output: output.txt
```

### Memory Optimization
- **Streaming Processing**: Handles large files without loading everything into memory
- **Chunk Processing**: Processes data in manageable chunks
- **Progress Checkpoints**: Regular progress updates for long operations

### Error Recovery
- **File Validation**: Checks input files before processing
- **Graceful Failures**: Detailed error messages for troubleshooting
- **Interrupt Handling**: Clean shutdown on Ctrl+C

## Batch Processing

### Process Multiple Files

```python
from pathlib import Path
from tools.nav_decoder import NavCodec

codec = NavCodec()
input_dir = Path("navdata_files")
output_dir = Path("decoded_files")

# Create output directory
output_dir.mkdir(exist_ok=True)

# Process all .nav files
for nav_file in input_dir.glob("*.nav"):
    output_file = output_dir / f"{nav_file.stem}.txt"
    try:
        codec.decode_file(nav_file, output_file)
        print(f"✓ {nav_file.name} decoded successfully")
    except Exception as e:
        print(f"✗ {nav_file.name} failed: {e}")
```

### Shell Script (Unix/Linux)

```bash
#!/bin/bash
# decode_all.sh - Process multiple navdata files

for file in *.nav; do
    if [ -f "$file" ]; then
        output="${file%.nav}.txt"
        python nav_decoder.py decode "$file" "$output"
        echo "Processed: $file -> $output"
    fi
done
```

## Integration Examples

### Data Analysis Pipeline

```python
import pandas as pd
from tools.nav_decoder import NavCodec

def analyze_navdata(nav_file):
    # Decode navdata
    codec = NavCodec()
    decoded_file = "temp_decoded.txt"
    codec.decode_file(nav_file, decoded_file)
    
    # Parse runway data
    runways = []
    with open(decoded_file, 'r') as f:
        for line in f:
            if line.startswith('RWY'):
                # Parse runway record
                runway_data = parse_runway(line)
                runways.append(runway_data)
    
    # Create DataFrame for analysis
    df = pd.DataFrame(runways)
    return df
```

### Web Service Integration

```python
from flask import Flask, request, send_file
from tools.nav_decoder import NavCodec
import tempfile
import os

app = Flask(__name__)
codec = NavCodec()

@app.route('/decode', methods=['POST'])
def decode_navdata():
    if 'file' not in request.files:
        return 'No file provided', 400
    
    file = request.files['file']
    
    # Create temporary files
    with tempfile.NamedTemporaryFile(suffix='.nav', delete=False) as input_temp:
        file.save(input_temp.name)
        
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as output_temp:
            try:
                codec.decode_file(input_temp.name, output_temp.name)
                return send_file(output_temp.name, as_attachment=True)
            finally:
                os.unlink(input_temp.name)
                os.unlink(output_temp.name)
```

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| "Input file not found" | Wrong file path | Check file path and permissions |
| "Input file is empty" | Corrupted file | Verify file integrity |
| "Decode failed" | Wrong XOR key | Try different XOR key values |
| Memory errors | Very large files | Use streaming mode or chunk processing |

### Debug Mode

```python
import logging
from tools.nav_decoder import NavCodec

# Enable debug logging
codec = NavCodec()
codec.logger.setLevel(logging.DEBUG)

# Run operation with detailed logs
codec.decode_file("navdata.nav", "output.txt")
```

### Performance Tuning

```python
from tools.nav_decoder import NavCodec, CodecConfig

# Optimized for large files
config = CodecConfig(
    progress_steps=100,     # More frequent updates
    header_threshold=64     # Faster header detection
)

codec = NavCodec(config)
```

## Next Steps

- **[See usage examples](./examples.md)** - Practical scenarios and workflows
- **[Learn about data formats](../guide/)** - Understand the decoded content
- **[Explore integration options](./examples.md#integration)** - Use with other tools
