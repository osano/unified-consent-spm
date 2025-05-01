#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path


def update_package_swift(version: str, checksum: str):
    try:
        # Get the root directory path (parent of scripts directory)
        root_dir = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        scripts_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        
        # Read the template from the scripts directory
        template_path = scripts_dir / "Package.swift.template"
        if not template_path.exists():
            print(f"Error: Template file not found at {template_path}", file=sys.stderr)
            sys.exit(1)
            
        template_content = template_path.read_text()
        
        # Replace placeholders
        updated_content = template_content.replace("{{{version}}}", version)
        updated_content = updated_content.replace("{{{checksum}}}", checksum)
        
        # Write to Package.swift
        package_path = root_dir / "Package.swift"
        package_path.write_text(updated_content)
        print(f"Successfully updated Package.swift with version {version} and checksum {checksum}")
        
    except Exception as e:
        print(f"Error updating Package.swift: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Update Package.swift with new version and checksum")
    parser.add_argument("--version", required=True, help="Version number (e.g. 1.0.0)")
    parser.add_argument("--checksum", required=True, help="Package checksum")
    
    args = parser.parse_args()
    update_package_swift(args.version, args.checksum)

if __name__ == "__main__":
    main() 