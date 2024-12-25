#!/bin/bash

# Exit on error
set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}Starting build and publish process...${NC}"

# Function to build and publish a package
build_and_publish() {
    local package_dir=$1
    echo -e "${BLUE}Processing ${package_dir}...${NC}"
    
    # Navigate to package directory
    cd "$package_dir"
    
    # Clean previous builds
    rm -rf dist/ build/ *.egg-info/
    
    # Build the package
    echo -e "${BLUE}Building distribution...${NC}"
    python3 -m pip install --upgrade build
    python3 -m build
    
    # Upload to PyPI
    echo -e "${BLUE}Uploading to PyPI...${NC}"
    python3 -m pip install --upgrade twine
    
    # Try to upload and handle existing version case
    if python3 -m twine upload dist/* 2>&1 | grep -q "File already exists"; then
        echo -e "${YELLOW}Version already exists on PyPI - skipping${NC}"
    else
        echo -e "${GREEN}Successfully uploaded to PyPI${NC}"
    fi
    
    # Navigate back
    cd ..
    
    echo -e "${GREEN}Finished processing ${package_dir}${NC}"
}

# Build and publish mt5-grpc-proto first
echo -e "${BLUE}Publishing mt5-grpc-proto package...${NC}"
build_and_publish "mt5_grpc_proto"

# Then build and publish mt5-grpc-server
echo -e "${BLUE}Publishing mt5-grpc-server package...${NC}"
build_and_publish "mt5_grpc_server"

echo -e "${GREEN}All packages have been processed!${NC}" 