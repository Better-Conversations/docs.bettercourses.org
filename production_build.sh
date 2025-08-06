#!/bin/bash

# So that conf.py is set correctly to show TODO items
export BUILD_TYPE="Production"

# Build the HTML and LaTeX PDF versions
make html 
# make latexpdf

# Copy the resulting PDF to the build directory


# These directories are not included in the build process by default
# So we copy them manually
# You should be able to use html_extra_path in conf.py to add more files but I couldn't get it to work
cp -r source/downloads build/html/
cp -r source/documentation/downloads build/html/documentation/
cp source/robots.txt build/html/
cp source/404.html build/html/404.html

# Copy the resulting PDF to the build directory
# cp build/latex/betterconversations-foundation.pdf build/html/documentation/

# Index documentation in Typesense for search
echo ""
echo "Indexing documentation in Typesense..."
if [ -f ".env.typesense" ] && [ -f "typesense-scraper-config.json" ]; then
    # Try Docker scraper first
    if command -v docker &> /dev/null; then
        sh scripts/index-typesense.sh
    # Fallback to Python scraper if Docker not available
    elif command -v python3 &> /dev/null; then
        echo "Docker not available, using Python scraper..."
        pip install -q typesense beautifulsoup4 python-dotenv
        python3 scripts/index-typesense.py
    else
        echo "Warning: Neither Docker nor Python available for Typesense indexing"
        echo "Skipping search indexing step"
    fi
else
    echo "Typesense configuration not found, skipping indexing"
    echo "To enable search indexing, create .env.typesense and typesense-scraper-config.json"
fi
