#!/usr/bin/env python3
"""
NAV File Encoder/Decoder

A tool for encoding and decoding .nav files using XOR encryption.
Supports batch processing and configurable encoding parameters.
"""

import os
import sys
import argparse
import logging
from typing import Tuple, Optional
from pathlib import Path
from dataclasses import dataclass

@dataclass
class CodecConfig:
    """Configuration for the NAV codec operations."""
    xor_key: int = 0x85
    header_threshold: int = 128
    content_line_threshold: int = 30
    progress_steps: int = 20
    encoding: str = 'utf-8'

class ProgressTracker:
    """Handles progress tracking and display."""
    
    def __init__(self, total_size: int, steps: int = 20):
        self.total_size = total_size
        self.steps = steps
        self.current_step = 0
        self.step_size = max(1, total_size // steps)
        self.checkpoints = [self.step_size * i for i in range(steps + 1)]
        
    def update(self, current_pos: int) -> Optional[int]:
        """Update progress and return percentage if milestone reached."""
        if self.current_step < len(self.checkpoints) and current_pos >= self.checkpoints[self.current_step]:
            self.current_step += 1
            return (self.current_step * 100) // self.steps
        return None

class NavCodecError(Exception):
    """Custom exception for NAV codec operations."""
    pass

class NavCodec:
    """Main class for NAV file encoding and decoding operations."""
    
    def __init__(self, config: CodecConfig = None):
        self.config = config or CodecConfig()
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """Setup logging configuration."""
        logger = logging.getLogger('nav_codec')
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger
    
    def _separate_header_content(self, data: bytes) -> Tuple[bytes, bytes]:
        """Separate header (ASCII) from binary content."""
        header_bytes = bytearray()
        content_start = 0
        
        for i, byte_val in enumerate(data):
            if byte_val < self.config.header_threshold:
                header_bytes.append(byte_val)
                content_start = i + 1
            else:
                break
        
        return bytes(header_bytes), data[content_start:]
    
    def _separate_text_header_content(self, lines: list) -> Tuple[str, str]:
        """Separate header from content in text file based on line length."""
        header = ''
        content = ''
        content_started = False
        
        for line in lines:
            if len(line) > self.config.content_line_threshold:
                content_started = True
            
            if content_started:
                content += line
            else:
                header += line
        
        return header, content
    
    def decode_file(self, input_path: Path, output_path: Path) -> None:
        """Decode a .nav file to text format."""
        try:
            self.logger.info(f"Starting decode operation: {input_path} -> {output_path}")
            
            if not input_path.exists():
                raise NavCodecError(f"Input file not found: {input_path}")
            
            # Read binary data
            with open(input_path, 'rb') as file:
                raw_data = bytearray(file.read())
            
            if not raw_data:
                raise NavCodecError(f"Input file is empty: {input_path}")
            
            # Separate header and content
            header_bytes, content_data = self._separate_header_content(raw_data)
            
            # Decode content with progress tracking
            decoded_bytes = bytearray()
            progress = ProgressTracker(len(content_data), self.config.progress_steps)
            
            for i, byte_val in enumerate(content_data):
                # Update progress
                percentage = progress.update(i)
                if percentage:
                    self.logger.info(f"Progress: {percentage}%")
                
                # Decode byte
                if byte_val < self.config.header_threshold:
                    decoded_bytes.append(byte_val)
                else:
                    decoded_byte = byte_val ^ self.config.xor_key
                    decoded_bytes.append(decoded_byte)
            
            # Convert bytes back to string
            header = header_bytes.decode(self.config.encoding)
            content = decoded_bytes.decode(self.config.encoding)
            
            # Write output
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding=self.config.encoding, newline='') as file:
                file.write(header + content)
            
            self.logger.info(f"Decode completed successfully. Output: {output_path}")
            
        except Exception as e:
            raise NavCodecError(f"Decode failed: {e}") from e
    
    def encode_file(self, input_path: Path, output_path: Path) -> None:
        """Encode a text file to .nav format."""
        try:
            self.logger.info(f"Starting encode operation: {input_path} -> {output_path}")
            
            if not input_path.exists():
                raise NavCodecError(f"Input file not found: {input_path}")
            
            # Read text data
            with open(input_path, 'r', encoding=self.config.encoding, newline='') as file:
                lines = file.readlines()
            
            if not lines:
                raise NavCodecError(f"Input file is empty: {input_path}")
            
            # Separate header and content
            header, content = self._separate_text_header_content(lines)
            
            # Write output
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'wb') as file:
                # Write header as-is (encode as bytes)
                header_bytes = header.encode(self.config.encoding)
                for byte_val in header_bytes:
                    file.write(bytes([byte_val]))
                
                # Encode content with progress tracking
                content_bytes = content.encode(self.config.encoding)
                progress = ProgressTracker(len(content_bytes), self.config.progress_steps)
                
                for i, byte_val in enumerate(content_bytes):
                    # Update progress
                    percentage = progress.update(i)
                    if percentage:
                        self.logger.info(f"Progress: {percentage}%")
                    
                    # Encode byte
                    if byte_val not in {10, 13}:  # Preserve newlines
                        byte_val ^= self.config.xor_key
                    file.write(bytes([byte_val]))
            
            self.logger.info(f"Encode completed successfully. Output: {output_path}")
            
        except Exception as e:
            raise NavCodecError(f"Encode failed: {e}") from e
    
    def auto_process(self, directory: Path = None) -> None:
        """Automatically process files in directory based on naming convention."""
        if directory is None:
            directory = Path.cwd()
        
        self.logger.info(f"Auto-processing files in: {directory}")
        
        # Check for decode file
        decode_input = directory / "wait2decode.nav"
        if decode_input.exists():
            decode_output = directory / "already_decode.txt"
            self.decode_file(decode_input, decode_output)
        
        # Check for encode file
        encode_input = directory / "wait2encode.txt"
        if encode_input.exists():
            encode_output = directory / "already_encode.nav"
            self.encode_file(encode_input, encode_output)
        
        if not decode_input.exists() and not encode_input.exists():
            self.logger.info("No files found for auto-processing (wait2decode.nav or wait2encode.txt)")

def create_parser() -> argparse.ArgumentParser:
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="NAV File Encoder/Decoder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s auto                           # Auto-process files in current directory
  %(prog)s decode input.nav output.txt    # Decode NAV file to text
  %(prog)s encode input.txt output.nav    # Encode text file to NAV
  %(prog)s -k 0xFF encode input.txt out.nav  # Use custom XOR key
        """
    )
    
    parser.add_argument('command', choices=['auto', 'decode', 'encode'],
                        help='Operation to perform')
    parser.add_argument('input_file', nargs='?',
                        help='Input file path (not needed for auto mode)')
    parser.add_argument('output_file', nargs='?',
                        help='Output file path (not needed for auto mode)')
    parser.add_argument('-k', '--xor-key', type=lambda x: int(x, 0), default=0x85,
                        help='XOR key for encoding/decoding (default: 0x85)')
    parser.add_argument('-d', '--directory', type=Path, default=None,
                        help='Working directory (default: current directory)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose logging')
    parser.add_argument('--steps', type=int, default=20,
                        help='Number of progress steps (default: 20)')
    
    return parser

def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Setup configuration
    config = CodecConfig(
        xor_key=args.xor_key,
        progress_steps=args.steps
    )
    
    # Setup codec
    codec = NavCodec(config)
    if args.verbose:
        codec.logger.setLevel(logging.DEBUG)
    
    try:
        if args.command == 'auto':
            codec.auto_process(args.directory)
        
        elif args.command == 'decode':
            if not args.input_file or not args.output_file:
                parser.error("decode command requires input_file and output_file")
            codec.decode_file(Path(args.input_file), Path(args.output_file))
        
        elif args.command == 'encode':
            if not args.input_file or not args.output_file:
                parser.error("encode command requires input_file and output_file")
            codec.encode_file(Path(args.input_file), Path(args.output_file))
    
    except NavCodecError as e:
        codec.logger.error(f"Operation failed: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        codec.logger.info("Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        codec.logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
