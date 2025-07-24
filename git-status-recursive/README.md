# git-status-recursive

## Description
This script recursively explores directories up to a specified depth and runs `git status` in each directory that contains a Git repository. It provides a comprehensive overview of the status of multiple Git repositories in a directory tree.

## Requirements
- Bash
- Git
- Directory structure with multiple Git repositories

## Usage
```bash
bash git_status_recursive.sh <depth>
```

### Parameters
- `<depth>`: Maximum directory depth to explore (required)

### Examples
```bash
# Check Git status in current directory and 1 level deep
bash git_status_recursive.sh 1

# Check Git status in current directory and 2 levels deep
bash git_status_recursive.sh 2
```

## What it does
1. **Directory Traversal**: Recursively explores directories up to the specified depth
2. **Git Detection**: Identifies directories containing `.git` folders
3. **Status Display**: Runs `git status` in each Git repository found
4. **Path Highlighting**: Shows the current repository path in yellow color for better visibility
5. **Depth Control**: Limits exploration to prevent excessive recursion

## Output Format
- Repository paths are displayed in **yellow** color
- Standard `git status` output follows each path
- Non-Git directories are silently skipped

## Use Cases
- Managing multiple Git repositories in a workspace
- Quick overview of uncommitted changes across projects
- Batch checking repository status before major operations
- Development environment health checks
- Project portfolio management

## Features
- **Colored Output**: Enhanced readability with colored directory paths
- **Depth Limiting**: Prevents infinite recursion in complex directory structures
- **Silent Skipping**: Only shows output for actual Git repositories
- **Usage Help**: Built-in usage instructions for incorrect parameters