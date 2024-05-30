#!/bin/bash

# Set the directory path
directory="./screenshots"

# Delete files starting with "roblox"
rm -f "$directory/Roblox"*

# Print a message after deletion
echo "Files starting with 'Roblox' have been deleted in $directory."