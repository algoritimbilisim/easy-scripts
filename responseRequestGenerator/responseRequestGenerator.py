import os
import re

def find_java_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                yield os.path.join(root, file)

def extract_entity_info(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        if '@Entity' in content:
            package_match = re.search(r'package\s+([\w.]+)', content)
            class_name = re.search(r'class\s+(\w+)', content)
            fields = re.findall(r'private\s+(\w+(?:\s*<\s*\w+\s*>)?)\s+(\w+)', content)
            if package_match and class_name and fields:
                return package_match.group(1), class_name.group(1), fields
    return None, None, None

def create_pojo(package, class_name, fields, file_type, entity_file_path):
    pojo_content = f"""package {package};

import lombok.Data;
import java.util.UUID;

@Data
public class {class_name}{file_type} {{
{generate_fields(fields)}
}}
"""
    pojo_file = os.path.join(os.path.dirname(entity_file_path), f"{class_name}{file_type}.java")
    if not os.path.exists(pojo_file):
        with open(pojo_file, 'w') as file:
            file.write(pojo_content)
        print(f"Created {file_type}: {pojo_file}")
    else:
        print(f"{file_type} already exists: {pojo_file}")

def generate_fields(fields):
    return '\n'.join(f"    private {field_type} {field_name};" for field_type, field_name in fields)

def main(root_directory):
    for java_file in find_java_files(root_directory):
        package, entity_name, fields = extract_entity_info(java_file)
        if package and entity_name and fields:
            create_pojo(package, entity_name, fields, "Request", java_file)
            create_pojo(package, entity_name, fields, "Response", java_file)

if __name__ == "__main__":
    root_dir = input("Enter the root directory to search: ")
    main(root_dir)