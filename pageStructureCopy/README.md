# pageStructureCopy

## Description
This script copies the directory structure from a source directory to a target directory, creating only the folder hierarchy without copying files. It's useful for replicating directory structures for testing, organization, or template purposes.

## Requirements
- Python 3.x
- os module (built-in)
- Source directory that exists
- Write permissions for target directory

## Usage
```bash
python pageStructureCopy.py
```

## Configuration
Modify the source and target directories in the script:
```python
kaynak_dizin = 'src/views/pages'  # Source directory path
hedef_dizin = 'cypress/e2e'       # Target directory path
```

## What it does
1. **Directory Traversal**: Uses `os.walk()` to recursively traverse the source directory
2. **Path Calculation**: Calculates relative paths from source to maintain structure
3. **Directory Creation**: Creates corresponding directories in the target location
4. **Existence Check**: Checks if directories already exist before creating
5. **Progress Reporting**: Shows which directories are created or already exist

## Example
If you have the following source structure:
```
src/views/pages/
├── admin/
│   ├── users/
│   └── settings/
├── public/
│   ├── home/
│   └── about/
└── dashboard/
    ├── analytics/
    └── reports/
```

After running the script, the target structure will be:
```
cypress/e2e/
├── admin/
│   ├── users/
│   └── settings/
├── public/
│   ├── home/
│   └── about/
└── dashboard/
    ├── analytics/
    └── reports/
```

## Output
For each directory operation, the script displays:
```
Oluşturuluyor: cypress/e2e/admin/users
Zaten mevcut: cypress/e2e/public
Oluşturuluyor: cypress/e2e/dashboard/analytics
```

## Use Cases
- **Test Structure Setup**: Creating test directory structures that mirror source code
- **Project Templates**: Setting up project scaffolding with predefined folder structures
- **Backup Preparation**: Creating directory structures for organized backups
- **Migration Planning**: Preparing target structures before file migration
- **Development Environment**: Setting up consistent folder structures across environments
- **Documentation Organization**: Creating structured documentation hierarchies

## Features
- **Non-destructive**: Only creates directories, doesn't modify existing ones
- **Recursive Processing**: Handles nested directory structures of any depth
- **Relative Path Preservation**: Maintains the exact directory hierarchy
- **Existence Awareness**: Skips directories that already exist
- **Progress Feedback**: Shows real-time creation status
- **Cross-platform**: Works on Windows, macOS, and Linux

## Customization
- **Source Path**: Change `kaynak_dizin` to your desired source directory
- **Target Path**: Change `hedef_dizin` to your desired target directory
- **Filtering**: Add conditions to skip certain directories
- **Logging**: Enhance output with more detailed logging
- **Error Handling**: Add try-catch blocks for robust error handling

## Safety Notes
- The script only creates directories, it doesn't copy files
- Existing directories are preserved and not overwritten
- Ensure you have write permissions for the target directory
- Verify source and target paths before running