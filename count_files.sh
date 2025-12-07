#!/bin/bash
files=$(find /etc -type f)
count=$(echo "$files" | wc -l)
echo "Number of files in /etc: $count"
