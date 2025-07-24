# remove-console-logs

## Description
This script removes console logging statements from JavaScript/TypeScript files. It intelligently handles single-line and multi-line console statements, including `console.log`, `console.error`, `console.warn`, and `console.info`, while preserving code structure and formatting.

## Requirements
- Python 3.x
- re module (built-in)
- Target JavaScript/TypeScript files
- Write permissions for the files

## Usage
```bash
python remove_console_logs.py
```

## Configuration
Modify the file path in the script:
```python
file_path = 'path/to/your/file.js'  # Change this to your target file
```

## What it does
1. **File Reading**: Reads the entire content of the specified file
2. **Pattern Detection**: Identifies console logging statements using regex patterns
3. **Multi-line Handling**: Properly handles console statements that span multiple lines
4. **Parentheses Counting**: Uses parentheses counting to determine statement boundaries
5. **Semicolon Cleanup**: Removes trailing semicolons associated with console statements
6. **File Writing**: Writes the cleaned content back to the file

## Supported Console Methods
The script removes the following console methods:
- `console.log()`
- `console.error()`
- `console.warn()`
- `console.info()`

## Examples

### Before
```javascript
function calculateTotal(items) {
  console.log('Starting calculation');
  let total = 0;
  
  for (let item of items) {
    console.log('Processing item:', item);
    total += item.price;
  }
  
  console.error('Debug info:', {
    itemCount: items.length,
    total: total
  });
  
  console.warn('Calculation complete');
  return total;
}
```

### After
```javascript
function calculateTotal(items) {
  let total = 0;
  
  for (let item of items) {
    total += item.price;
  }
  
  return total;
}
```

## Multi-line Console Handling
The script properly handles complex multi-line console statements:

### Before
```javascript
console.log(
  'Complex object:',
  {
    user: userData,
    timestamp: new Date(),
    nested: {
      value: someValue
    }
  }
);
```

### After
```javascript
// Completely removed
```

## Features
- **Intelligent Parsing**: Uses parentheses counting for accurate statement detection
- **Multi-line Support**: Handles console statements spanning multiple lines
- **Semicolon Cleanup**: Removes associated semicolons to prevent syntax errors
- **Preserve Formatting**: Maintains original code indentation and structure
- **Safe Removal**: Only removes complete console statements, not partial matches
- **Multiple Methods**: Supports all common console logging methods
- **Regex-based**: Uses efficient regular expressions for pattern matching

## Algorithm Details
1. **Initial Detection**: Uses regex to find console method calls
2. **Boundary Detection**: Counts opening and closing parentheses
3. **Multi-line Tracking**: Continues parsing until parentheses are balanced
4. **Content Extraction**: Extracts the complete console statement
5. **Semicolon Handling**: Checks for and removes trailing semicolons
6. **Replacement**: Replaces the entire statement with empty string

## Use Cases
- **Production Cleanup**: Remove debug statements before production deployment
- **Code Optimization**: Clean up development code for better performance
- **Security**: Remove potentially sensitive information from console logs
- **Code Review**: Prepare code for review by removing debug statements
- **Build Process**: Integrate into build pipelines for automatic cleanup
- **Legacy Code**: Clean up old codebases with excessive logging
- **Performance**: Reduce bundle size by removing unnecessary console calls

## File Types Supported
- JavaScript files (`.js`)
- TypeScript files (`.ts`)
- Vue.js files (`.vue`) - JavaScript sections
- React JSX files (`.jsx`)
- Any text file containing JavaScript console statements

## Safety Features
- **Backup Recommendation**: Always backup files before running or if you use git be sure to check the changes via `git diff`
- **Complete Statement Removal**: Only removes complete, valid console statements
- **Syntax Preservation**: Maintains valid JavaScript syntax after removal
- **Non-destructive to Logic**: Only removes logging, preserves business logic

## Limitations
- **String Literals**: Won't remove console statements within string literals
- **Dynamic Calls**: May not handle dynamically constructed console calls
- **Minified Code**: Not designed for minified/obfuscated code

## Customization
- **File Path**: Change the target file path
- **Console Methods**: Add or remove console methods to target
- **Pattern Matching**: Modify regex patterns for specific requirements
- **Output Handling**: Add logging or progress reporting
- **Batch Processing**: Extend to process multiple files
- **Backup Creation**: Add automatic backup functionality

## Integration
This script can be integrated into:
- **Build Systems**: Webpack, Rollup, Vite plugins
- **CI/CD Pipelines**: Automated code cleanup
- **Git Hooks**: Pre-commit hooks for automatic cleanup
- **IDE Extensions**: Custom editor extensions
- **Linting Tools**: ESLint custom rules