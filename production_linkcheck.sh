#! /bin/bash

# Check the main web site links
linkchecker --check-extern --no-status --no-warnings https://betterconversations.foundation/

# List of URLs to check
urls=(
    "https://betterconversations.foundation/l/license"
    "https://betterconversations.foundation/l/attribution"
    "https://betterconversations.foundation/l/masters"
    "https://betterconversations.foundation/l/flightplans"
    "https://betterconversations.foundation/l/support"
    "https://betterconversations.foundation/l/zoombor"
    "https://betterconversations.foundation/l/handbook"
    "https://betterconversations.foundation/l/overview"
    "https://betterconversations.foundation/docs/"
)

# Check each URL and store the exit code
exit_code=0
for url in "${urls[@]}"; do
    if ! linkchecker --no-warnings --no-status --recursion-level=1 "$url" > /dev/null 2>&1; then
        echo "Error checking: $url"
        exit_code=1
    fi
done

# Exit with failure if any checks failed
exit $exit_code

