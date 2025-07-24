# javaToTxtConverter

## Description
This script converts all Java files in a directory (including subdirectories) to text files with .txt extension. It's useful for creating text copies of Java source code for documentation, analysis, or backup purposes. It may help for batch uploads to systems that don't support .java files such as AI inference systems.

## Requirements
- Bash
- find command
- cp command
- Java project with .java files

## Usage
```bash
bash javaToTxtConverter.sh
```

## What it does
1. **File Discovery**: Uses `find` to locate all .java files recursively
2. **Name Generation**: Creates corresponding .txt filenames by replacing .java extension
3. **File Copying**: Copies each .java file to its .txt equivalent
4. **Progress Reporting**: Shows which files have been created

## Example
If you have the following structure:
```
src/
├── main/
│   └── java/
│       ├── User.java
│       └── service/
│           └── UserService.java
```

After running the script:
```
src/
├── main/
│   └── java/
│       ├── User.java
│       ├── User.txt
│       └── service/
│           ├── UserService.java
│           └── UserService.txt
```

## Output
For each converted file, the script displays:
```
Created: ./src/main/java/User.txt
Created: ./src/main/java/service/UserService.txt
```

## Use Cases
- **Documentation**: Creating text versions for documentation systems
- **Code Analysis**: Preparing files for text analysis tools
- **Backup**: Creating readable backups of source code
- **Migration**: Preparing code for systems that don't handle .java files
- **Text Processing**: Enabling text-based tools to process Java code
- **Archive Creation**: Creating text archives of source code

## Features
- **Recursive Processing**: Handles nested directory structures
- **Preserve Structure**: Maintains the original directory hierarchy
- **Non-destructive**: Original .java files remain unchanged
- **Simple Operation**: No configuration required
- **Progress Feedback**: Shows conversion progress