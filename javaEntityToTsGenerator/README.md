# javaEntityToTsGenerator

## Description
This script automatically converts Java JPA entity classes to TypeScript interfaces, maintaining the same package structure and handling complex type mappings. It supports multiprocessing for faster conversion of large codebases.

## Requirements
- Python 3.x
- Java project with JPA entity classes
- multiprocessing support

## Usage
```bash
python javaEntityToTsGenerator.py
```

The script will prompt for the root directory (e.g., `src/main/java`).

## What it does
1. **Entity Discovery**: Scans for Java files with `@Entity` annotation
2. **Field Extraction**: Extracts private fields and their types using regex
3. **Type Mapping**: Converts Java types to TypeScript equivalents
4. **Import Generation**: Creates proper import statements for entity relationships
5. **Structure Preservation**: Maintains the same package structure in TypeScript
6. **Parallel Processing**: Uses multiprocessing for faster conversion

## Type Mappings
- `String` → `string`
- `Integer`, `int`, `Long`, `long`, `Double`, `double`, `Float`, `float` → `number`
- `Boolean`, `boolean` → `boolean`
- `LocalDate`, `LocalDateTime`, `Date` → `Date`
- `List<T>`, `Set<T>` → `T[]`
- Custom entity types → Imported TypeScript interfaces

## Output Structure
```
ts_models/
├── com/
│   └── example/
│       └── entity/
│           ├── User.ts
│           ├── Order.ts
│           └── Product.ts
```

## Example Conversion

### Java Entity
```java
package com.example.entity;

@Entity
public class User {
    private Long id;
    private String name;
    private LocalDate birthDate;
    private List<Order> orders;
}
```

### Generated TypeScript
```typescript
import type { Order } from './Order';

export interface User {
  id?: number;
  name?: string;
  birthDate?: Date;
  orders?: Order[];
}
```

## Features
- **Automatic Imports**: Generates relative import paths for entity relationships
- **Optional Fields**: All fields are marked as optional with `?`
- **Generic Support**: Handles generic types like `List<T>`, `Set<T>`
- **Package Structure**: Preserves Java package hierarchy
- **Multiprocessing**: Faster processing for large projects
- **Relationship Handling**: Properly imports related entities

## Use Cases
- Frontend-backend type synchronization
- API client generation
- Type-safe frontend development
- Documentation generation
- Code migration projects