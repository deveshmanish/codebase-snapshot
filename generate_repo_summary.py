import os
import argparse

def print_directory_structure(startpath, output_file, prefix=""):
    """Prints the directory structure similar to the 'tree' command."""
    try:
        items = sorted(os.listdir(startpath))
    except PermissionError:
        output_file.write(f"{prefix}[Permission Denied]\n")
        return

    for i, item in enumerate(items):
        path = os.path.join(startpath, item)
        is_last = i == len(items) - 1
        connector = "└── " if is_last else "├── "
        output_file.write(f"{prefix}{connector}{item}\n")

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            print_directory_structure(path, output_file, prefix + extension)

def print_file_contents(filepath, output_file):
    """Prints the file path as a comment and its content."""
    output_file.write("-" * 20 + "\n")
    output_file.write(f"# File: {filepath}\n")
    output_file.write("-" * 20 + "\n")
    try:
        # Attempt to read as text
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            output_file.write(content)
    except (UnicodeDecodeError, PermissionError):
        # Handle binary files or permission errors
        output_file.write(f"# [Could not read file content (binary or permission denied)]\n")
    except Exception as e:
         output_file.write(f"# [Error reading file: {e}]\n")
    output_file.write("\n\n") # Add separation

def should_exclude(path, exclude_patterns):
    """Checks if a path should be excluded based on patterns."""
    abs_path = os.path.abspath(path)
    for pattern in exclude_patterns:
        # Simple check, can be made more robust with fnmatch or pathlib
        if pattern in abs_path:
            return True
    return False

def main(repo_path, output_filename):
    """Main function to orchestrate the summary generation."""
    exclude_patterns = [
        output_filename,
        '.git', 'node_modules', '__pycache__', 'build', 'dist',
        '.log', '.tmp', '.swp', '.DS_Store'
    ]

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write("=== Repository Structure (tree-like) ===\n")
        print_directory_structure(repo_path, output_file)
        output_file.write("\n=== File Contents ===\n\n")

        for root, dirs, files in os.walk(repo_path):
            # Modify dirs in-place to skip excluded directories during traversal
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d), exclude_patterns)]

            for file in files:
                filepath = os.path.join(root, file)
                # Check if the file itself should be excluded
                if not should_exclude(filepath, exclude_patterns):
                     print_file_contents(filepath, output_file)

    print(f"Repository summary generated in '{output_filename}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a summary of a repository's structure and file contents.")
    parser.add_argument("repo_path", nargs='?', default=".", help="Path to the repository (default: current directory)")
    parser.add_argument("-o", "--output", default="repo_contents_summary.txt", help="Output filename (default: repo_contents_summary.txt)")
    args = parser.parse_args()

    main(args.repo_path, args.output)
