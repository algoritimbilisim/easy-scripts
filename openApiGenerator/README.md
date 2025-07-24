# openApiGenerator

## Description
This script automatically generates OpenAPI 3.0 specification files for Spring Boot REST controllers. It analyzes Java controller files and creates comprehensive API documentation in YAML format, including endpoints, request/response schemas, and parameter definitions.

## Requirements
- Python 3.x
- PyYAML library (`pip install pyyaml`)
- Java Spring Boot project with controllers
- Request and Response DTO classes
- Standard REST controller structure

## Usage
```bash
python openApiGenerator.py
```

## What it does
1. **Controller Discovery**: Scans for Java controller files in the project
2. **Endpoint Analysis**: Extracts REST endpoints and HTTP methods
3. **Parameter Parsing**: Identifies path parameters, query parameters, and request bodies
4. **Schema Generation**: Creates OpenAPI schemas from Request/Response classes
5. **Documentation Creation**: Generates complete OpenAPI YAML files
6. **Missing Endpoint Detection**: Suggests standard REST endpoints that might be missing

## Generated OpenAPI Features
- **Complete Specification**: OpenAPI 3.0 compliant YAML files
- **Endpoint Documentation**: All REST endpoints with proper HTTP methods
- **Schema Definitions**: Request and Response object schemas
- **Parameter Documentation**: Path, query, and body parameters
- **Response Codes**: Standard HTTP response codes (200, 201, 400, 404, 500)
- **Type Mapping**: Java types mapped to OpenAPI types
- **Pagination Support**: Special handling for paginated responses

## Supported Java Types
| Java Type | OpenAPI Type | Format |
|-----------|--------------|--------|
| String | string | - |
| Integer/int | integer | int32 |
| Long/long | integer | int64 |
| Double/double | number | double |
| Float/float | number | float |
| Boolean/boolean | boolean | - |
| LocalDate | string | date |
| LocalDateTime | string | date-time |
| BigDecimal | number | - |
| UUID | string | uuid |

## Endpoint Classification
The script automatically classifies endpoints based on method names and HTTP methods:
- **GET All**: `getAll*`, `findAll*`, `listAll*`
- **GET By ID**: `get*ById`, `find*WithId`
- **CREATE**: `create*`, `add*`, `save*`, `store*`
- **UPDATE**: `update*`, `edit*`, `modify*`
- **DELETE**: `delete*`, `remove*`, `destroy*`
- **SEARCH**: `search*`, `find*`, `query*`, `filter*`

## Output Structure
```
api_contracts/
├── User_api.yaml
├── Product_api.yaml
└── Order_api.yaml
```

## Example Generated API
```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: Get all users
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/UserResponse'
    post:
      summary: Create user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRequest'
components:
  schemas:
    UserRequest:
      type: object
      properties:
        name:
          type: string
        email:
          type: string
    UserResponse:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
        email:
          type: string
```

## Features
- **Strategy Pattern**: Modular design with pluggable components
- **Type Safety**: Proper Java to OpenAPI type conversion
- **Pagination Aware**: Handles Spring Data Page responses
- **Generic Support**: Supports generic types like `List<T>`, `Page<T>`
- **Missing Endpoint Detection**: Suggests standard CRUD endpoints
- **Flexible Architecture**: Easy to extend and customize
- **Error Handling**: Graceful handling of parsing errors

## Architecture Components
- **EndpointClassifierStrategy**: Classifies endpoint types
- **EndpointDetectorStrategy**: Detects missing standard endpoints
- **JavaTypeConverter**: Converts Java types to OpenAPI types
- **ParameterParser**: Parses method parameters
- **JavaClassParser**: Parses Java class files
- **JavaControllerParser**: Parses controller files
- **ReturnTypeHandler**: Handles method return types

## Use Cases
- **API Documentation**: Generate comprehensive API documentation
- **Frontend Development**: Provide clear API contracts for frontend teams
- **Testing**: Create API specifications for automated testing
- **Client Generation**: Generate API clients from OpenAPI specs
- **API Governance**: Ensure consistent API design patterns
- **Integration**: Facilitate third-party integrations

## Customization
- **Type Mappings**: Modify `StandardJavaTypeConverter` for custom type mappings
- **Endpoint Classification**: Extend `RegexEndpointClassifier` for custom patterns
- **Response Handling**: Customize `StandardReturnTypeHandler` for specific response types
- **Parameter Parsing**: Enhance `RegexParameterParser` for complex parameter patterns

## Configuration
The script can be configured by modifying:
- Root directory path (default: `src/main/java`)
- Output directory (default: `api_contracts`)
- Type conversion mappings
- Endpoint classification patterns