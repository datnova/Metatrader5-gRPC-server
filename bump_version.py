#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

def bump_version(version: str, bump_type: str) -> str:
    major, minor, patch = map(int, version.strip('"').split('.'))
    
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    
    return f'"{major}.{minor}.{patch}"'

def update_setup_files(bump_type: str):
    setup_files = [
        'mt5_grpc_server/setup.py',
        'mt5_grpc_proto/setup.py'
    ]
    
    version_pattern = re.compile(r'version="(\d+\.\d+\.\d+)"')
    
    for setup_file in setup_files:
        path = Path(setup_file)
        if not path.exists():
            print(f"Warning: {setup_file} not found")
            continue
            
        content = path.read_text()
        match = version_pattern.search(content)
        
        if match:
            old_version = match.group(0)
            new_version = f'version={bump_version(match.group(1), bump_type)}'
            updated_content = content.replace(old_version, new_version)
            path.write_text(updated_content)
            print(f"Updated {setup_file}: {old_version} -> {new_version}")
        else:
            print(f"Warning: No version found in {setup_file}")

def main():
    parser = argparse.ArgumentParser(description='Bump version numbers in setup.py files')
    parser.add_argument('bump_type', choices=['major', 'minor', 'patch'],
                      help='Which version number to increment')
    
    args = parser.parse_args()
    update_setup_files(args.bump_type)

if __name__ == '__main__':
    main() 