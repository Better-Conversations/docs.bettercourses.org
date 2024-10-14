#!/bin/bash

# So that conf.py is set correctly to show TODO items
export BUILD_TYPE="Production"

make html 

# These directories are not included in the build process by default
# So we copy them manually
# You should be able to use html_extra_path in conf.py to add more files but I couldn't get it to work
cp -r source/downloads build/html/
cp -r source/documentation/downloads build/html/documentation/
cp source/robots.txt build/html/
cp source/404.html build/html/404.html
