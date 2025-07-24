#!/usr/bin/env python3

import os
import re
import sys

def remove_console_logs(file_path):
    """
    Remove console.log, console.error, console.warn, and console.info statements from a file
    using parenthesis counting to handle multi-line statements.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Pattern to match console.log, console.error, console.warn, and console.info statements
    pattern = r'console\.(log|error|warn|info)\s*\('
    
    # Find all matches
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        return False  # No console statements found
    
    # Process the file content from end to beginning to avoid index issues
    new_content = content
    modified = False
    
    for match in reversed(matches):
        start_pos = match.start()
        
        # Find the end of the statement by counting parentheses
        pos = match.end()
        paren_count = 1  # We start with one open parenthesis
        
        while pos < len(content) and paren_count > 0:
            if content[pos] == '(':
                paren_count += 1
            elif content[pos] == ')':
                paren_count -= 1
            pos += 1
        
        # If we found the closing parenthesis, check for semicolon
        if paren_count == 0 and pos < len(content) and content[pos] == ';':
            pos += 1
        
        # Remove the console statement
        new_content = new_content[:start_pos] + new_content[pos:]
        modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        return True
    
    return False

def main():
    # Find all .ts, .tsx, and .vue files in the ogyp-frontend/src directory
    src_dir = 'ogyp-frontend/src'
    modified_count = 0
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(('.ts', '.tsx', '.vue')):
                file_path = os.path.join(root, file)
                
                try:
                    if remove_console_logs(file_path):
                        print(f"Modified: {file_path}")
                        modified_count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    print(f"Completed! Modified {modified_count} files.")

if __name__ == "__main__":
    main()
