# Encoding Table

PFPX Navdata files use a custom XOR-based encoding system. The navigation data is encoded using a character mapping table that transforms readable ASCII text into binary data.

## Character Mapping

Through reverse engineering, we've determined the following encoding relationships:

| Hex Code | Character | Hex Code | Character |
|----------|-----------|----------|-----------|
| A5 | Space (` `) | B5 | 0 |
| A4 | ! | B4 | 1 |
| A7 | " | B7 | 2 |
| A6 | # | B6 | 3 |
| A1 | $ | B1 | 4 |
| A0 | % | B0 | 5 |
| A3 | & | B3 | 6 |
| A2 | ' | B2 | 7 |
| AD | ( | BD | 8 |
| AC | ) | BC | 9 |
| AF | * | BF | : |
| AE | + | BE | ; |
| A9 | , | B9 | < |
| A8 | – | B8 | = |
| AB | . | BB | > |
| AA | / | BA | ? |

| Hex Code | Character | Hex Code | Character |
|----------|-----------|----------|-----------|
| C5 | @ | D5 | P |
| C4 | A | D4 | Q |
| C7 | B | D7 | R |
| C6 | C | D6 | S |
| C1 | D | D1 | T |
| C0 | E | D0 | U |
| C3 | F | D3 | V |
| C2 | G | D2 | W |
| CD | H | DD | X |
| CC | I | DC | Y |
| CF | J | DF | Z |
| CE | K | DE | [ |
| C9 | L | D9 | \ |
| C8 | M | D8 | ] |
| CB | N | DB | ^ |
| CA | O | DA | _ |

| Hex Code | Character | Hex Code | Character |
|----------|-----------|----------|-----------|
| E5 | ` | F5 | p |
| E4 | a | F4 | q |
| E7 | b | F7 | r |
| E6 | c | F6 | s |
| E1 | d | F1 | t |
| E0 | e | F0 | u |
| E3 | f | F3 | v |
| E2 | g | F2 | w |
| ED | h | FD | x |
| EC | i | FC | y |
| EF | j | FF | z |
| EE | k | FE | { |
| E9 | l | F9 | \| |
| E8 | m | F8 | } |
| EB | n | FB | ~ |
| EA | o | FA | DEL |

## Encoding Method

The encoding process works as follows:

1. **XOR Operation**: Each byte is XORed with the key `0x85`
2. **Character Mapping**: The result maps to the above character table
3. **Header Preservation**: File headers remain in plaintext
4. **Line Structure**: Each line represents one navigation data entry

## Key Properties

- **XOR Key**: `0x85` (decimal 133)
- **Reversible**: The same operation decodes the data
- **ASCII Compatible**: Maps to standard ASCII character set
- **Binary Safe**: Preserves data integrity

## Usage Notes

::: warning Important
- Only the navigation data content is encoded
- File headers and metadata remain in plaintext
- Newline characters (CR/LF) are preserved during encoding
- The encoding is case-sensitive and position-dependent
:::

## Example Transformation

Here's a simple example of how a character gets encoded:

```
Original character: 'A' (ASCII 65, hex 0x41)
XOR with 0x85: 0x41 ^ 0x85 = 0xC4
Lookup in table: 0xC4 = 'A'
```

For the reverse (decoding):
```
Encoded byte: 0xC4
XOR with 0x85: 0xC4 ^ 0x85 = 0x41
ASCII result: 0x41 = 'A'
```

## Next Steps

- **[Learn the decoding process](./decoding-process.md)** - Apply this knowledge practically
- **[Use our Python tools](../tools/python-decoder.md)** - Automate encoding/decoding
- **[Understand file structure](./file-structure.md)** - See how encoded data is organized
