# Usage Examples

Practical examples and workflows for working with PFPX navdata files using our Python decoder.

## Getting Started Examples

### Your First Decode

```bash
# Download a navdata file to your working directory
# Run the decoder
python nav_decoder.py decode navdata.nav decoded_output.txt

# View the results
head -20 decoded_output.txt
```

Expected output:
```
PFPX NAVDATA
NG2509
2025/09/04
2025/10/01
NAVIGRAPH

RWY ZBAA01   12467197359ASP+40058914+116617658
RWY ZBAA19   12467197179ASP+40073556+116598889
...
```

### Auto-Processing Workflow

```bash
# Setup standard file names
cp your_navdata.nav wait2decode.nav

# Run auto-processing
python nav_decoder.py auto

# Results appear automatically
ls -la already_decode.txt
```

## Data Analysis Examples

### Extract Runway Information

```python
#!/usr/bin/env python3
"""Extract runway data from PFPX navdata file."""

from tools.nav_decoder import NavCodec
import re
from pathlib import Path

def extract_runways(navdata_file, output_file):
    """Extract all runway records to a separate file."""
    
    # Decode the navdata file
    codec = NavCodec()
    decoded_file = "temp_decoded.txt"
    codec.decode_file(Path(navdata_file), Path(decoded_file))
    
    # Extract runway records
    runways = []
    with open(decoded_file, 'r') as f:
        for line in f:
            if line.startswith('RWY'):
                runways.append(line.strip())
    
    # Write runway data
    with open(output_file, 'w') as f:
        f.write(f"Found {len(runways)} runways\n")
        f.write("=" * 50 + "\n")
        for runway in runways:
            f.write(runway + "\n")
    
    print(f"Extracted {len(runways)} runways to {output_file}")

# Usage
extract_runways("navdata.nav", "runways_only.txt")
```

### Airport Analysis

```python
#!/usr/bin/env python3
"""Analyze airports and their runways."""

from tools.nav_decoder import NavCodec
from collections import defaultdict
import re

def analyze_airports(navdata_file):
    """Analyze airport data and runway counts."""
    
    # Decode file
    codec = NavCodec()
    decoded_file = "temp_decoded.txt"
    codec.decode_file(navdata_file, decoded_file)
    
    # Count runways per airport
    airport_runways = defaultdict(list)
    
    with open(decoded_file, 'r') as f:
        for line in f:
            if line.startswith('RWY'):
                # Parse: RWY ICAO## ...
                parts = line.split()
                if len(parts) >= 2:
                    icao_runway = parts[1]  # e.g., "ZBAA01"
                    icao = icao_runway[:4]  # "ZBAA"
                    runway = icao_runway[4:] # "01"
                    airport_runways[icao].append(runway)
    
    # Display results
    print(f"Airport Analysis ({len(airport_runways)} airports)")
    print("=" * 50)
    
    for icao in sorted(airport_runways.keys())[:10]:  # Top 10
        runways = airport_runways[icao]
        print(f"{icao}: {len(runways)} runways - {', '.join(runways)}")

# Usage
analyze_airports("navdata.nav")
```

## Batch Processing Examples

### Process Multiple Files

```python
#!/usr/bin/env python3
"""Batch process multiple navdata files."""

from tools.nav_decoder import NavCodec
from pathlib import Path
import sys

def batch_decode(input_dir, output_dir):
    """Decode all .nav files in a directory."""
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory
    output_path.mkdir(exist_ok=True)
    
    # Find all .nav files
    nav_files = list(input_path.glob("*.nav"))
    if not nav_files:
        print(f"No .nav files found in {input_dir}")
        return
    
    print(f"Found {len(nav_files)} files to process")
    
    codec = NavCodec()
    successful = 0
    failed = 0
    
    for nav_file in nav_files:
        output_file = output_path / f"{nav_file.stem}_decoded.txt"
        
        try:
            codec.decode_file(nav_file, output_file)
            print(f"✓ {nav_file.name}")
            successful += 1
        except Exception as e:
            print(f"✗ {nav_file.name}: {e}")
            failed += 1
    
    print(f"\nResults: {successful} successful, {failed} failed")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python batch_decode.py <input_dir> <output_dir>")
        sys.exit(1)
    
    batch_decode(sys.argv[1], sys.argv[2])
```

### Shell Script for Unix/Linux

```bash
#!/bin/bash
# batch_process.sh - Process multiple navdata files

INPUT_DIR="navdata_files"
OUTPUT_DIR="decoded_files"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Process each .nav file
for file in "$INPUT_DIR"/*.nav; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .nav)
        output="$OUTPUT_DIR/${filename}_decoded.txt"
        
        echo "Processing: $filename"
        python nav_decoder.py decode "$file" "$output"
        
        if [ $? -eq 0 ]; then
            echo "✓ Success: $filename"
        else
            echo "✗ Failed: $filename"
        fi
    fi
done

echo "Batch processing complete!"
```

## Integration Examples

### Flask Web Service

```python
#!/usr/bin/env python3
"""Web service for navdata decoding."""

from flask import Flask, request, jsonify, send_file
from tools.nav_decoder import NavCodec
import tempfile
import os
from pathlib import Path

app = Flask(__name__)
codec = NavCodec()

@app.route('/api/decode', methods=['POST'])
def decode_api():
    """API endpoint to decode navdata files."""
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Create temporary files
    with tempfile.NamedTemporaryFile(suffix='.nav', delete=False) as input_temp:
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as output_temp:
            try:
                # Save uploaded file
                file.save(input_temp.name)
                
                # Decode
                codec.decode_file(Path(input_temp.name), Path(output_temp.name))
                
                # Return decoded file
                return send_file(
                    output_temp.name,
                    as_attachment=True,
                    download_name='decoded_navdata.txt'
                )
                
            except Exception as e:
                return jsonify({'error': str(e)}), 500
            
            finally:
                # Clean up
                try:
                    os.unlink(input_temp.name)
                    os.unlink(output_temp.name)
                except:
                    pass

@app.route('/api/info', methods=['POST'])
def info_api():
    """Extract basic info from navdata file."""
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    # Read first few lines for header info
    file.seek(0)
    lines = []
    for i in range(5):
        line = file.readline().decode('utf-8', errors='ignore').strip()
        if line:
            lines.append(line)
    
    if len(lines) >= 5:
        return jsonify({
            'database': lines[0],
            'version': lines[1],
            'effective_date': lines[2],
            'expiration_date': lines[3],
            'provider': lines[4]
        })
    else:
        return jsonify({'error': 'Invalid navdata file format'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Data Pipeline with Pandas

```python
#!/usr/bin/env python3
"""Data analysis pipeline using pandas."""

import pandas as pd
from tools.nav_decoder import NavCodec
import re
from pathlib import Path

class NavDataAnalyzer:
    """Analyze PFPX navdata using pandas."""
    
    def __init__(self):
        self.codec = NavCodec()
    
    def decode_and_parse(self, navdata_file):
        """Decode file and parse into structured data."""
        
        # Decode
        decoded_file = "temp_decoded.txt"
        self.codec.decode_file(Path(navdata_file), Path(decoded_file))
        
        # Parse different record types
        runways = []
        waypoints = []
        airways = []
        
        with open(decoded_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('RWY'):
                    runways.append(self.parse_runway(line))
                elif line.startswith('WPT'):
                    waypoints.append(self.parse_waypoint(line))
                elif line.startswith('AWY'):
                    airways.append(self.parse_airway(line))
        
        return {
            'runways': pd.DataFrame(runways),
            'waypoints': pd.DataFrame(waypoints),
            'airways': pd.DataFrame(airways)
        }
    
    def parse_runway(self, line):
        """Parse runway record."""
        # RWY ZBAA01   12467197359ASP+40058914+116617658
        pattern = r'RWY (\w{4})(\d{2})\s+(\d+)(\d{3})(\d{3})ASP([+-]\d{8})([+-]\d{9})'
        match = re.match(pattern, line)
        
        if match:
            return {
                'icao': match.group(1),
                'runway': match.group(2),
                'length_ft': int(match.group(3)),
                'width_ft': int(match.group(4)),
                'heading': int(match.group(5)),
                'latitude': int(match.group(6)) / 1_000_000,
                'longitude': int(match.group(7)) / 1_000_000
            }
        return {}
    
    def parse_waypoint(self, line):
        """Parse waypoint record (simplified)."""
        parts = line.split()
        if len(parts) >= 3:
            return {
                'identifier': parts[1],
                'type': parts[2][0] if len(parts[2]) > 0 else '',
                'raw_line': line
            }
        return {}
    
    def parse_airway(self, line):
        """Parse airway record (simplified)."""
        parts = line.split()
        if len(parts) >= 2:
            return {
                'identifier': parts[1],
                'raw_line': line
            }
        return {}

# Usage example
def main():
    analyzer = NavDataAnalyzer()
    data = analyzer.decode_and_parse("navdata.nav")
    
    # Analyze runways
    runways_df = data['runways']
    print(f"Total runways: {len(runways_df)}")
    print(f"Average runway length: {runways_df['length_ft'].mean():.0f} ft")
    print(f"Longest runway: {runways_df['length_ft'].max()} ft")
    
    # Top airports by runway count
    runway_counts = runways_df.groupby('icao').size().sort_values(ascending=False)
    print("\nTop 10 airports by runway count:")
    print(runway_counts.head(10))

if __name__ == "__main__":
    main()
```

## Advanced Workflows

### Automated Processing with Monitoring

```python
#!/usr/bin/env python3
"""Monitor directory for new navdata files and auto-process."""

import time
from pathlib import Path
from tools.nav_decoder import NavCodec
import logging

class NavdataMonitor:
    """Monitor directory for new navdata files."""
    
    def __init__(self, watch_dir, output_dir, check_interval=60):
        self.watch_dir = Path(watch_dir)
        self.output_dir = Path(output_dir)
        self.check_interval = check_interval
        self.codec = NavCodec()
        self.processed_files = set()
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def process_new_files(self):
        """Check for and process new .nav files."""
        nav_files = set(self.watch_dir.glob("*.nav"))
        new_files = nav_files - self.processed_files
        
        for nav_file in new_files:
            output_file = self.output_dir / f"{nav_file.stem}_decoded.txt"
            
            try:
                self.logger.info(f"Processing: {nav_file.name}")
                self.codec.decode_file(nav_file, output_file)
                self.logger.info(f"Completed: {nav_file.name}")
                self.processed_files.add(nav_file)
                
            except Exception as e:
                self.logger.error(f"Failed to process {nav_file.name}: {e}")
    
    def run(self):
        """Start monitoring loop."""
        self.logger.info(f"Starting monitor: {self.watch_dir}")
        self.logger.info(f"Output directory: {self.output_dir}")
        self.logger.info(f"Check interval: {self.check_interval}s")
        
        self.output_dir.mkdir(exist_ok=True)
        
        try:
            while True:
                self.process_new_files()
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            self.logger.info("Monitor stopped by user")

# Usage
if __name__ == "__main__":
    monitor = NavdataMonitor("input_files", "decoded_files", 30)
    monitor.run()
```

## Next Steps

- **[Learn about data formats](../guide/)** - Understand what the decoded data contains
- **[Explore the Python decoder](./python-decoder.md)** - Advanced features and configuration
- **[Study specific data sections](../guide/runways.md)** - Detailed format specifications
