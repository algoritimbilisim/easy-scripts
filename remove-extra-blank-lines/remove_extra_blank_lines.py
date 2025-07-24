#!/usr/bin/env python3

import os
import re

def remove_extra_blank_lines(file_path):
    """
    Removes consecutive blank lines in a file and replaces them with a single blank line.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace 2 or more consecutive blank lines with a single blank line
    new_content = re.sub(r'\n{3,}', '\n\n', content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        return True

    return False

def main():
    src_dir = 'src'
    modified_count = 0

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(('.ts', '.tsx', '.vue')):
                file_path = os.path.join(root, file)
                try:
                    if remove_extra_blank_lines(file_path):
                        print(f"Modified: {file_path}")
                        modified_count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"Completed! Modified {modified_count} files.")

if __name__ == "__main__":
    main()
