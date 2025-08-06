#!/bin/bash

# Typesense DocSearch Scraper for Better Conversations Foundation Documentation
# This script runs the official Typesense DocSearch scraper to index Sphinx documentation

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Typesense DocSearch Scraper...${NC}"

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Docker is not installed or not available.${NC}"
    echo "Please install Docker to run the scraper."
    exit 1
fi

# Check if required files exist
if [ ! -f ".env.typesense" ]; then
    echo -e "${RED}Missing .env.typesense file${NC}"
    echo "Please create .env.typesense with your Typesense credentials"
    exit 1
fi

if [ ! -f "typesense-scraper-config.json" ]; then
    echo -e "${RED}Missing typesense-scraper-config.json file${NC}"
    echo "Please create typesense-scraper-config.json with scraper configuration"
    exit 1
fi

# Check if build directory exists
if [ ! -d "build/html" ]; then
    echo -e "${YELLOW}Warning: build/html directory not found${NC}"
    echo "Make sure to run the Sphinx build before indexing"
    echo "Run: sh production_build.sh"
    exit 1
fi

echo -e "${GREEN}Configuration files found. Starting scraper...${NC}"

# Run the Typesense DocSearch scraper
# Using version 0.9.1 which is the latest stable version
docker run -it --rm \
  --env-file=.env.typesense \
  -e "CONFIG=$(cat typesense-scraper-config.json | jq -r tostring)" \
  typesense/docsearch-scraper:0.9.1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Typesense indexing completed successfully!${NC}"
else
    echo -e "${RED}✗ Typesense indexing failed${NC}"
    exit 1
fi