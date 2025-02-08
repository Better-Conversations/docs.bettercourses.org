#!/bin/bash

# So that conf.py is set correctly to show TODO items
export BUILD_TYPE="Development"

rm -Rf build

# If we're running in a container, Git is going to get upset
# Because ownership of the files is going to be different than
# the user that is running the container. 
if [ -d "/workspace" ]; then
  git config --global --add safe.directory /workspaces/bcf-website
fi

# Install requirements just in case they have changed
pip install -r requirements.txt

sphinx-autobuild source build/html/
