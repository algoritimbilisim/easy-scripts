import os
import re
import multiprocessing

def find_java_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                yield os.path.join(root, file)

def extract_entity_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if '@Entity' in content:
            class_name = re.search(r'class\s+(\w+)', content)
            package_name = re.search(r'package\s+([\w.]+);', content)
            fields = re.findall(r'private\s+(\w+(?:\s*<\s*\w+\s*>)?)\s+(\w+);', content)
            if class_name and fields:
                return class_name.group(1), fields, package_name.group(1) if package_name else None
    return None, None, None

def create_ts_file(class_name, fields, output_dir, entities, package_path, entity_paths):
    # Create the directory structure based on the package path
    ts_dir = os.path.join(output_dir, *package_path.split('.'))
    os.makedirs(ts_dir, exist_ok=True)

    imports = generate_imports(fields, entities, class_name, entity_paths, package_path)
    ts_content = f"""{imports}

export interface {class_name} {{
{generate_ts_fields(fields, entities)}
}}
"""
    ts_file = os.path.join(ts_dir, f"{class_name}.ts")
    with open(ts_file, 'w', encoding='utf-8') as file:
        file.write(ts_content)
    print(f"Created TypeScript file: {ts_file}")

def generate_imports(fields, entities, current_class, entity_paths, current_package):
    imports = set()
    for field_type, _ in fields:
        base_type = field_type.split('<')[0]
        if base_type in entities and base_type != current_class:
            # Get the package path for the imported entity
            if base_type in entity_paths:
                import_package = entity_paths[base_type]
                # Calculate the relative import path
                if import_package == current_package:
                    # Same package, use local import
                    imports.add(f"import type {{ {base_type} }} from './{base_type}';")
                else:
                    # Different package, calculate relative path
                    current_parts = current_package.split('.')
                    import_parts = import_package.split('.')

                    # Find common prefix
                    common_prefix_len = 0
                    for i in range(min(len(current_parts), len(import_parts))):
                        if current_parts[i] == import_parts[i]:
                            common_prefix_len += 1
                        else:
                            break

                    # Build relative path
                    up_levels = len(current_parts) - common_prefix_len
                    down_path = '/'.join(import_parts[common_prefix_len:])

                    if up_levels > 0:
                        rel_path = '../' * up_levels + down_path
                    else:
                        rel_path = './' + down_path

                    imports.add(f"import type {{ {base_type} }} from '{rel_path}/{base_type}';")
    return '\n'.join(sorted(imports))

def generate_ts_fields(fields, entities):
    return '\n'.join(f"  {field_name}: {java_to_ts_type(field_type, entities)};" for field_type, field_name in fields)

def java_to_ts_type(java_type, entities):
    if '<' in java_type:
        base_type, inner_type = re.match(r'(\w+)\s*<\s*(\w+)\s*>', java_type).groups()
        return f"{java_to_ts_type(base_type, entities)}<{java_to_ts_type(inner_type, entities)}>"
    type_mappings = {
        "String": "string", "int": "number", "Integer": "number",
        "long": "number", "Long": "number",
        "float": "number", "Float": "number",
        "double":"number",  "Double": "number",
        "boolean": "boolean", "Boolean": "boolean",
        "byte": "boolean", "Byte": "boolean",
        "short": "number", "Short": "number",
        "BigDecimal": "number", "BigInteger": "number",
        "LocalTime": "Date", "ZonedDateTime": "Date", "LocalDate": "Date",
        "Time": "Date", "Timestamp": "Date", "Instant": "Date",
        "byte[]": "string", "Byte[]": "string", "byte[][]": "string", "Byte[][]": "string",
        "char[]": "string", "Character[]": "string", "char[][]": "string", "Character[][]": "string",
        "String[]": "string[]", "String[][]": "string[]",
        "List<String>": "string[]", "List<Integer>": "number[]", "List<Long>": "number[]",
        "List<Long>": "number[]", "List<Float>": "number[]", "List<Double>": "number[]",
        "List<BigDecimal>": "number[]", "List<BigInteger>": "number[]",
        "List<Boolean>": "boolean[]", "List<Byte>": "boolean[]", "List<Short>": "number[]",
        "List<LocalTime>": "Date[]", "List<ZonedDateTime>": "Date[]", "List<LocalDate>": "Date[]",
        "List<Time>": "Date[]", "List<Timestamp>": "Date[]", "List<Instant>": "Date[]",
        "List<byte[]>": "string[]", "List<byte[][]>": "string[]",
        "List<char[]>": "string[]", "List<char[][]>": "string[]",
        "List<String[]>": "string[][]", "List<String[][]>": "string[][]",
        "List<List<String>>": "string[][]", "List<List<Integer>>": "number[][]", "List<List<Long>>": "number[][]",
        "List<List<Long>>": "number[][]", "List<List<Float>>": "number[][]", "List<List<Double>>": "number[][]",
        "List<List<BigDecimal>>": "number[][]", "List<List<BigInteger>>": "number[][]",
        "char": "string", "Character": "string",
        "List": "Array<any>", "Set": "Set<any>", "UUID": "string",
        "Date": "Date", "DateTime": "Date", "LocalDate": "Date", "ZonedDateTime": "Date"
    }
    return type_mappings.get(java_type, java_type if java_type in entities else "any")

def process_file(args):
    java_file, output_dir, entities, entity_paths = args
    class_name, fields, package_name = extract_entity_info(java_file)
    if class_name and fields and package_name:
        create_ts_file(class_name, fields, output_dir, entities, package_name, entity_paths)

def main(root_directory):
    output_dir = os.path.join(root_directory, 'ts_models')
    os.makedirs(output_dir, exist_ok=True)

    entities = set()
    entity_paths = {}

    # First pass: collect all entity names and their package paths
    for java_file in find_java_files(root_directory):
        class_name, _, package_name = extract_entity_info(java_file)
        if class_name and package_name:
            entities.add(class_name)
            entity_paths[class_name] = package_name

    # Second pass: generate TypeScript files with proper imports
    with multiprocessing.Pool() as pool:
        pool.map(process_file, [(f, output_dir, entities, entity_paths) for f in find_java_files(root_directory)])

if __name__ == "__main__":
    root_dir = input("Enter the root directory to search (e.g., src/main/java): ")
    main(root_dir)
    print("\nTypeScript models have been generated in the 'ts_models' directory with the same package structure as Java.")

