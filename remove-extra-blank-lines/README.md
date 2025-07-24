# remove-extra-blank-lines

## Description
This script removes excessive consecutive blank lines from TypeScript, TSX, and Vue.js files, replacing multiple blank lines with a single blank line. It helps maintain clean and consistent code formatting across your project.

## Requirements
- Python 3.x
- os and re modules (built-in)
- Source directory containing target files
- Write permissions for the files

## Usage
```bash
python remove_extra_blank_lines.py
```

## Configuration
Modify the source directory in the script:
```python
src_dir = 'src'  # Change this to your source directory
```

## What it does
1. **Directory Traversal**: Recursively walks through the specified source directory
2. **File Filtering**: Processes only `.ts`, `.tsx`, and `.vue` files
3. **Content Analysis**: Reads file content and identifies consecutive blank lines
4. **Pattern Replacement**: Uses regex to replace 3+ consecutive newlines with 2 newlines
5. **File Update**: Writes the cleaned content back to the file if changes were made
6. **Progress Reporting**: Shows which files were modified and total count

## Supported File Types
- **TypeScript**: `.ts` files
- **TypeScript React**: `.tsx` files
- **Vue.js**: `.vue` files

## Examples

### Before
```typescript
function calculateTotal(items: Item[]) {
  let total = 0;



  for (const item of items) {
    total += item.price;




    console.log(`Added ${item.name}`);
  }


  return total;
}
```

### After
```typescript
function calculateTotal(items: Item[]) {
  let total = 0;

  for (const item of items) {
    total += item.price;

    console.log(`Added ${item.name}`);
  }

  return total;
}
```

## Features
- **Selective Processing**: Only processes specific file types
- **Non-destructive**: Preserves single blank lines and content structure
- **Efficient**: Only writes to files that actually need changes
- **Progress Tracking**: Shows real-time processing status
- **Error Handling**: Gracefully handles file access errors
- **Encoding Support**: Handles UTF-8 encoded files properly
- **Recursive Processing**: Processes nested directory structures

## Algorithm Details
1. **Pattern Matching**: Uses regex `r'\n{3,}'` to find 3 or more consecutive newlines
2. **Replacement**: Replaces matches with exactly 2 newlines (`\n\n`)
3. **Change Detection**: Compares original and modified content
4. **Conditional Writing**: Only writes to file if content actually changed

## Output
The script provides detailed feedback:
```
Modified: src/components/UserPanel.vue
Modified: src/services/ApiService.ts
Modified: src/types/User.tsx
Completed! Modified 3 files.
```

## Use Cases
- **Code Cleanup**: Remove excessive whitespace from legacy code
- **Pre-commit Hooks**: Ensure consistent formatting before commits
- **Code Review Preparation**: Clean up code before review submissions
- **Project Migration**: Standardize formatting when migrating projects
- **Team Standards**: Enforce consistent blank line usage across team
- **Build Process**: Integrate into build pipelines for automatic cleanup
- **IDE Integration**: Use as external tool in development environments

## Project Structure
```
project/
├── src/
│   ├── components/
│   │   ├── UserPanel.vue
│   │   └── ProductList.tsx
│   ├── services/
│   │   └── ApiService.ts
│   └── types/
│       └── User.ts
└── remove_extra_blank_lines.py
```

## Safety Features
- **Backup Recommendation**: Always backup files before running or if you use git be sure to check the changes via `git diff`
- **Error Handling**: Continues processing even if individual files fail
- **Content Preservation**: Only removes excessive blank lines, preserves all other content
- **Encoding Safety**: Properly handles UTF-8 encoding
- **Change Validation**: Only modifies files that actually need changes

## Customization
- **Source Directory**: Change `src_dir` to target different directories
- **File Extensions**: Modify the file extension filter in the condition
- **Blank Line Policy**: Adjust regex pattern for different blank line rules
- **Output Verbosity**: Add or remove progress messages
- **Batch Processing**: Extend to process multiple directories
- **Backup Creation**: Add automatic backup functionality

## Integration
This script can be integrated with:
- **Git Hooks**: Pre-commit hooks for automatic formatting
- **CI/CD Pipelines**: Automated code cleanup in build processes
- **IDE Tools**: External tools in development environments
- **Build Scripts**: Part of project build and deployment scripts
- **Code Quality Tools**: Integration with linting and formatting tools
- **Team Workflows**: Standardized development processes

## Performance
- **Efficient Processing**: Only reads and writes files that need changes
- **Memory Optimized**: Processes files individually, not all at once
- **Fast Regex**: Uses optimized regular expressions for pattern matching
- **Minimal I/O**: Reduces file system operations through change detection

## Error Handling
The script handles various error scenarios:
- **File Access Errors**: Permission issues or locked files
- **Encoding Issues**: Non-UTF-8 files or encoding problems
- **Directory Access**: Missing or inaccessible directories
- **Disk Space**: Insufficient space for file modifications

## Limitations
- **File Type Specific**: Only processes `.ts`, `.tsx`, and `.vue` files
- **UTF-8 Encoding**: Assumes UTF-8 encoding for all files
- **Single Directory**: Processes one source directory at a time
- **No Backup**: Doesn't create automatic backups (manual backup recommended)