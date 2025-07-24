# responseRequestGenerator

## Description
This script automatically generates Request and Response POJO (Plain Old Java Object) classes for Java entities. It scans for `@Entity` annotated classes and creates corresponding Request and Response DTOs using Lombok's `@Data` annotation, following Spring Boot best practices.

## Requirements
- Python 3.x
- os and re modules (built-in)
- Java project with JPA entities
- Entities annotated with `@Entity`
- Lombok library in the project
- Write permissions for the target directory

## Usage
```bash
python responseRequestGenerator.py
```

The script will prompt you to enter the root directory to search for entities.

## What it does
1. **Entity Discovery**: Recursively searches for Java files with `@Entity` annotation
2. **Package Extraction**: Extracts package declaration from entity files
3. **Class Analysis**: Identifies class name and field definitions
4. **Field Parsing**: Extracts private fields with their types and names
5. **POJO Generation**: Creates Request and Response classes with Lombok annotations
6. **File Creation**: Saves generated POJOs to appropriate package structure

## Generated POJO Structure

### Request Class
```java
package com.example.dto.request;

import lombok.Data;

@Data
public class EntityNameRequest {
    private String fieldName;
    private Integer fieldNumber;
    private Boolean fieldFlag;
    // ... other fields
}
```

### Response Class
```java
package com.example.dto.response;

import lombok.Data;

@Data
public class EntityNameResponse {
    private String fieldName;
    private Integer fieldNumber;
    private Boolean fieldFlag;
    // ... other fields
}
```

## Entity Requirements
Your entities should follow this structure:
```java
package com.example.entity;

import javax.persistence.*;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    
    private String username;
    private String email;
    private Boolean active;
    
    // getters and setters...
}
```

## Features
- **Automatic Discovery**: Finds all entities in the specified directory tree
- **Package Preservation**: Maintains proper package structure for DTOs
- **Field Extraction**: Automatically extracts all private fields
- **Type Support**: Handles various Java types including generics
- **Lombok Integration**: Uses `@Data` annotation for automatic getters/setters
- **Dual Generation**: Creates both Request and Response classes
- **Proper Imports**: Includes necessary import statements
- **Naming Convention**: Follows standard DTO naming patterns

## Supported Field Types
The script automatically detects and supports:
- Primitive types: `int`, `long`, `boolean`, `double`, `float`
- Wrapper types: `Integer`, `Long`, `Boolean`, `Double`, `Float`
- String type: `String`
- Generic types: `List<String>`, `Set<Integer>`, etc.
- Custom object types
- Date and time types

## Example

### Input Entity
```java
package com.example.entity;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "products")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    
    private String name;
    private Double price;
    private Boolean available;
    private LocalDateTime createdAt;
    private List<String> tags;
    
    // getters and setters...
}
```

### Generated Request
```java
package com.example.dto.request;

import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;

@Data
public class ProductRequest {
    private Long id;
    private String name;
    private Double price;
    private Boolean available;
    private LocalDateTime createdAt;
    private List<String> tags;
}
```

### Generated Response
```java
package com.example.dto.response;

import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;

@Data
public class ProductResponse {
    private Long id;
    private String name;
    private Double price;
    private Boolean available;
    private LocalDateTime createdAt;
    private List<String> tags;
}
```

## Project Structure
```
project/
├── src/main/java/
│   ├── entity/
│   │   ├── User.java
│   │   ├── Product.java
│   │   └── Order.java
│   └── dto/
│       ├── request/
│       │   ├── UserRequest.java      # Generated
│       │   ├── ProductRequest.java   # Generated
│       │   └── OrderRequest.java     # Generated
│       └── response/
│           ├── UserResponse.java     # Generated
│           ├── ProductResponse.java  # Generated
│           └── OrderResponse.java    # Generated
└── responseRequestGenerator.py
```

## Use Cases
- **API Development**: Generate DTOs for REST API endpoints
- **Data Transfer**: Create objects for data transfer between layers
- **Code Consistency**: Ensure all DTOs follow the same pattern
- **Boilerplate Reduction**: Eliminate manual DTO creation
- **Project Setup**: Bootstrap DTO layer for new projects
- **Refactoring**: Update multiple DTOs with new patterns
- **Team Standardization**: Enforce consistent DTO structure

## Output
For each entity found, the script:
- Displays the entity being processed
- Shows the generated Request and Response file paths
- Reports successful POJO creation

```
Processing entity: User
Generated: /path/to/dto/request/UserRequest.java
Generated: /path/to/dto/response/UserResponse.java

Processing entity: Product
Generated: /path/to/dto/request/ProductRequest.java
Generated: /path/to/dto/response/ProductResponse.java
```

## Customization
- **Package Structure**: Modify DTO package naming conventions
- **Class Templates**: Customize generated class structure
- **Field Filtering**: Add logic to exclude certain fields
- **Annotation Support**: Include additional annotations
- **Import Management**: Customize import statements
- **Naming Patterns**: Adjust DTO naming conventions

## Safety Features
- **Directory Validation**: Ensures target directories exist
- **Package Structure**: Creates proper package hierarchy
- **Error Handling**: Graceful handling of file system errors
- **Field Validation**: Validates extracted field information

## Limitations
- **Field Detection**: Relies on specific field declaration patterns
- **Package Convention**: Follows specific package naming
- **Lombok Dependency**: Requires Lombok library in the project
- **Single Entity File**: Processes one entity per file
- **Standard Annotations**: Expects standard JPA annotations