# PFPX Navdata Format Documentation

Welcome to the complete guide for understanding and working with PFPX navigation data files.

## What is PFPX Navdata?

PFPX (Professional Flight Planner X) uses specialized navigation data files in a proprietary binary format. These files contain essential information for flight planning including:

- Airport and runway data
- Navigation aids (VOR, NDB, DME)
- Waypoints and intersections
- Airways and routes
- Standard Instrument Departures (SID)
- Standard Terminal Arrival Routes (STAR)

## Key Features

::: info Important Notice
As of now, neither Aerosoft nor Navigraph have published official specifications for the PFPX data format. All analysis and documentation presented here is based on personal research and reverse engineering. Accuracy is not guaranteed.
:::

### Data Sources

The navigation data typically comes from providers such as:
- **Navigraph** - Most common provider
- **Aerosoft** - Alternative data source

### File Characteristics

- **Format**: Binary files with XOR encryption
- **Extension**: `.nav`
- **Encoding**: Custom character mapping table
- **Structure**: Header (plaintext) + Encoded content
- **Update Cycle**: Follows AIRAC cycle (28-day intervals)

## Quick Start

1. **[Getting Started](./getting-started.md)** - Learn the basics and setup
2. **[File Structure](./file-structure.md)** - Understand the overall file organization
3. **[Decoding Process](./decoding-process.md)** - Learn how to decode the files
4. **[Tools](../tools/)** - Use our Python decoder tools

## Documentation Structure

This documentation is organized into several sections:

### Data Format
Learn about the technical aspects of the file format, encoding methods, and structure.

### Data Sections
Detailed breakdown of each data type within the files:
- Runways and airport information
- Navigation aids and waypoints
- Airways and route structure
- Departure and arrival procedures

### Additional Explanation
Specialized data for airspace management:
- FIR sectors and altitude constraints
- Heading ranges and restrictions

### Tools
Practical tools and utilities for working with PFPX navdata files.

## Contributing

Found an error or want to contribute? This documentation is continuously improved based on community research and findings.
