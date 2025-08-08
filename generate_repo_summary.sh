#!/bin/bash

# Check if a directory argument is provided, otherwise use current directory
REPO_DIR="${1:-.}"

# Define the output file name
OUTPUT_FILE="repo_contents_summary.txt"

# Start writing to the output file
{
    echo "=== Repository Structure (tree) ==="
    # Use the 'tree' command if available, otherwise fall back to 'find'
    if command -v tree &> /dev/null; then
        tree "$REPO_DIR"
    else
        echo "'tree' command not found. Using 'find' for structure (less visual)."
        # Basic structure using find and sed for indentation
        find "$REPO_DIR" | sed -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'
    fi
    echo ""
    echo "=== File Contents ==="
    echo ""

    # Find all files, excluding the output file itself and common binary/log files
    find "$REPO_DIR" -type f \
        ! -name "$OUTPUT_FILE" \
        ! -name "*.log" \
        ! -name "*.tmp" \
        ! -name "*.swp" \
        ! -name ".DS_Store" \
        ! -path "*/node_modules/*" \
        ! -path "*/.git/*" \
        ! -path "*/__pycache__/*" \
        ! -path "*/build/*" \
        ! -path "*/dist/*" \
        | while IFS= read -r file; do
            # Print a separator and the file path as a comment
            echo "--------------------"
            echo "# File: $file"
            echo "--------------------"
            # Print the content of the file
            cat "$file"
            # Add a newline for separation
            echo ""
            echo ""
        done
} > "$OUTPUT_FILE"

echo "Repository summary generated in '$OUTPUT_FILE'"
