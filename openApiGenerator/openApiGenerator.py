import os
import yaml
import re
import abc
from typing import Dict, List, Tuple, Any, Set, Optional

# Endpoint classifier strategy interface
class EndpointClassifierStrategy(abc.ABC):
    @abc.abstractmethod
    def classify(self, method_name: str, http_method: str) -> Dict[str, bool]:
        """Classify an endpoint based on method name and HTTP method."""
        pass

# Concrete endpoint classifier strategy using regex patterns
class RegexEndpointClassifier(EndpointClassifierStrategy):
    def __init__(self):
        # Define regex patterns for different endpoint types
        self.patterns = {
            'is_get_all': (r'^(?:getAll|findAll|listAll|retrieveAll|fetchAll|getAllEntities|getThemAll).*$', ['get']),
            'is_get_by_id': (r'^(?:get|find|retrieve|fetch).*(?:ById|WithId|ForId)$', ['get']),
            'is_create': (r'^(?:create|add|insert|save|store|register|post).*$', ['post', 'put']),
            'is_update': (r'^(?:update|edit|modify|change|alter|amend|revise).*$', ['put', 'patch']),
            'is_delete': (r'^(?:delete|remove|erase|destroy|eliminate).*$', ['delete']),
            'is_search': (r'^(?:search|find|query|filter|lookup|seek|browse).*$', ['get'])
        }
    
    def classify(self, method_name: str, http_method: str) -> Dict[str, bool]:
        """Classify an endpoint based on method name and HTTP method using regex patterns."""
        result = {key: False for key in self.patterns.keys()}
        
        for endpoint_type, (pattern, allowed_methods) in self.patterns.items():
            if http_method in allowed_methods and re.match(pattern, method_name, re.IGNORECASE):
                result[endpoint_type] = True
                
        return result

# Endpoint detector interface
class EndpointDetectorStrategy(abc.ABC):
    @abc.abstractmethod
    def detect_missing_endpoints(self, endpoints: List[Dict[str, Any]], entity_name: str) -> List[Dict[str, Any]]:
        """Detect and add missing standard endpoints."""
        pass

# Concrete endpoint detector using standard REST patterns
class StandardRESTEndpointDetector(EndpointDetectorStrategy):
    def __init__(self, classifier: EndpointClassifierStrategy):
        self.classifier = classifier
    
    def detect_missing_endpoints(self, endpoints: List[Dict[str, Any]], entity_name: str) -> List[Dict[str, Any]]:
        """Detect and add missing standard REST endpoints."""
        # Extract existing paths and methods
        existing_endpoints: Set[Tuple[str, str]] = {(endpoint['method'], endpoint['path']) for endpoint in endpoints}
        
        # Define standard endpoints that should exist based on controller methods
        standard_endpoints = [
            # Format: (condition_function, method, path, name_template, parameters_template, return_type_template)
            (
                lambda eps: any(ep.get('is_get_all', False) for ep in eps),
                'get', '/all', 
                f'getAll{entity_name}s',
                '',
                f'GlobalResponseMessage<ArrayList<{entity_name}Response>>'
            ),
            (
                lambda eps: any(ep.get('is_get_by_id', False) for ep in eps),
                'get', '/{id}', 
                f'get{entity_name}ById',
                f'@PathVariable UUID id',
                f'GlobalResponseMessage<{entity_name}Response>'
            ),
            (
                lambda eps: any(ep.get('is_create', False) for ep in eps),
                'post', '', 
                f'create{entity_name}',
                f'@RequestBody {entity_name}Request {entity_name.lower()}Request',
                f'GlobalResponseMessage<{entity_name}Response>'
            ),
            (
                lambda eps: any(ep.get('is_update', False) for ep in eps),
                'put', '/{id}', 
                f'update{entity_name}',
                f'@PathVariable UUID id, @RequestBody {entity_name}Request {entity_name.lower()}Request',
                f'GlobalResponseMessage<{entity_name}Response>'
            ),
            (
                lambda eps: any(ep.get('is_delete', False) for ep in eps),
                'delete', '/{id}', 
                f'delete{entity_name}',
                f'@PathVariable UUID id',
                f'GlobalResponseMessage<Boolean>'
            )
        ]
        
        # Add missing standard endpoints
        for condition_func, method, path, name_template, parameters_template, return_type_template in standard_endpoints:
            if condition_func(endpoints) and (method, path) not in existing_endpoints:
                # Create endpoint info based on the endpoint type
                endpoint_info = self.classifier.classify(name_template, method)
                
                # Create and add the missing endpoint
                endpoints.append({
                    'method': method,
                    'path': path,
                    'name': name_template,
                    'parameters': parameters_template,
                    'return_type': return_type_template,
                    **endpoint_info
                })
        
        return endpoints

# Java type converter interface
class JavaTypeConverter(abc.ABC):
    @abc.abstractmethod
    def to_openapi_type(self, java_type: str) -> Dict[str, Any]:
        """Convert Java type to OpenAPI type."""
        pass

# Concrete Java type converter
class StandardJavaTypeConverter(JavaTypeConverter):
    def __init__(self):
        # Define type mappings
        self.type_mapping = {
            'string': {'type': 'string'},
            'String': {'type': 'string'},
            'integer': {'type': 'integer'},
            'Integer': {'type': 'integer'},
            'int': {'type': 'integer'},
            'long': {'type': 'integer'},
            'Long': {'type': 'integer'},
            'Double': {'type': 'number'},
            'Float': {'type': 'number'},
            'double': {'type': 'number'},
            'float': {'type': 'number'},
            'Boolean': {'type': 'boolean'},
            'boolean': {'type': 'boolean'},
            'ZonedDateTime': {'type': 'string', 'format': 'date-time'},
            'LocalDateTime': {'type': 'string', 'format': 'date-time'},
            'LocalDate': {'type': 'string', 'format': 'date'},
            'Date': {'type': 'string', 'format': 'date-time'},
            'UUID': {'type': 'string'},
            'BigDecimal': {'type': 'number'}
        }
    
    def to_openapi_type(self, java_type: str) -> Dict[str, Any]:
        """Convert Java type to OpenAPI type."""
        # Check if it's a boolean reference
        if java_type == 'boolean':
            return {'type': 'boolean'}
        
        return self.type_mapping.get(java_type, {"$ref": f"#/components/schemas/{java_type}"})

# Parameter parser interface
class ParameterParser(abc.ABC):
    @abc.abstractmethod
    def parse(self, param: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """Parse a parameter string and extract type, name, and schema."""
        pass

# Concrete parameter parser using regex
class RegexParameterParser(ParameterParser):
    def parse(self, param: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """Parse a parameter string using regex patterns."""
        param = param.strip()
        if not param:
            return None, None, None
        
        # Initialize default parameter type
        param_type = 'query'
        
        # Extract Java type and parameter name using more robust patterns
        java_type = 'String'  # Default type
        param_name = None
        
        # Handle @PathVariable annotation
        if '@PathVariable' in param:
            param_type = 'path'
            # Try to extract parameter name and type with regex
            match = re.search(r'@PathVariable(?:\(.*?\))?\s+(?:final\s+)?([\w<>\[\],.]+)\s+([\w]+)', param)
            if match:
                java_type = match.group(1)
                param_name = match.group(2)
            else:
                # Try simpler pattern for just the name
                match = re.search(r'@PathVariable(?:\(.*?\))?\s+([\w]+)', param)
                if match:
                    param_name = match.group(1)
                else:
                    # Try to extract from @PathVariable("name")
                    match = re.search(r'@PathVariable\("([^"]+)"\)', param)
                    if match:
                        param_name = match.group(1)
        
        # Handle @RequestParam annotation
        elif '@RequestParam' in param:
            param_type = 'query'
            # Try to extract parameter name and type with regex
            match = re.search(r'@RequestParam(?:\(.*?\))?\s+(?:final\s+)?([\w<>\[\],.]+)\s+([\w]+)', param)
            if match:
                java_type = match.group(1)
                param_name = match.group(2)
            else:
                # Try simpler pattern for just the name
                match = re.search(r'@RequestParam(?:\(.*?\))?\s+([\w]+)', param)
                if match:
                    param_name = match.group(1)
                else:
                    # Try to extract from @RequestParam("name")
                    match = re.search(r'@RequestParam\("([^"]+)"\)', param)
                    if match:
                        param_name = match.group(1)
        
        # Handle @RequestBody annotation
        elif '@RequestBody' in param:
            param_type = 'body'
            # Try to extract parameter name and type with regex
            match = re.search(r'@RequestBody(?:\(.*?\))?\s+(?:final\s+)?([\w<>\[\],.]+)\s+([\w]+)', param)
            if match:
                java_type = match.group(1)
                param_name = match.group(2)
        
        # If we couldn't extract a parameter name, use the last word in the parameter string
        if not param_name:
            parts = param.split()
            if parts:
                param_name = parts[-1]
        
        # Determine parameter type based on Java type
        if java_type:
            if any(t in java_type for t in ['Long', 'Integer', 'int', 'long']):
                param_type_schema = 'integer'
            elif any(t in java_type for t in ['Double', 'Float', 'double', 'float', 'BigDecimal']):
                param_type_schema = 'number'
            elif any(t in java_type for t in ['Boolean', 'boolean']):
                param_type_schema = 'boolean'
            else:
                param_type_schema = 'string'
        else:
            param_type_schema = 'string'
        
        # Clean up param_name (remove trailing commas, etc.)
        if param_name:
            param_name = param_name.strip(',;')
        
        return param_type, param_name, param_type_schema

# Java class parser interface
class JavaClassParser(abc.ABC):
    @abc.abstractmethod
    def parse_file(self, file_content: str) -> Tuple[str, Dict[str, str]]:
        """Parse a Java class file and extract class name and properties."""
        pass

# Concrete Java class parser
class StandardJavaClassParser(JavaClassParser):
    def parse_file(self, file_content: str) -> Tuple[str, Dict[str, str]]:
        """Parse a Java class file using regex patterns."""
        class_name = re.search(r'class (\w+)', file_content).group(1)
        # Updated regex to capture the full type, including generics and annotations
        properties = re.findall(r'(?:@[^\n]+\s+)*private\s+([\w<>,\s\[\]]+)\s+(\w+)(?:\s*=\s*[^;]+)?;', file_content)
        
        property_dict = {}
        for type_name, prop_name in properties:
            # Normalize types to ensure consistent handling
            normalized_type = type_name.strip()
            
            # Handle date types with proper format
            if normalized_type in ['LocalDate']:
                property_dict[prop_name] = 'LocalDate'
            elif normalized_type in ['LocalDateTime', 'ZonedDateTime', 'Date']:
                property_dict[prop_name] = 'LocalDateTime'
            # Handle numeric types
            elif normalized_type in ['Integer', 'int']:
                property_dict[prop_name] = 'integer'
            elif normalized_type in ['Long', 'long']:
                property_dict[prop_name] = 'integer'
            elif normalized_type in ['Double', 'double', 'Float', 'float', 'BigDecimal']:
                property_dict[prop_name] = 'number'
            # Handle string types
            elif normalized_type == 'String':
                property_dict[prop_name] = 'string'
            elif normalized_type == 'UUID':
                property_dict[prop_name] = 'string'
            # Handle boolean types
            elif normalized_type in ['Boolean', 'boolean']:
                property_dict[prop_name] = 'boolean'
            # Handle collection types
            elif 'List<' in normalized_type or 'Set<' in normalized_type or 'Collection<' in normalized_type:
                # Extract the generic type
                generic_type = re.search(r'<([^>]+)>', normalized_type)
                if generic_type:
                    inner_type = generic_type.group(1).strip()
                    property_dict[prop_name] = f'List<{inner_type}>'
                else:
                    property_dict[prop_name] = 'array'
            # Handle map types
            elif 'Map<' in normalized_type:
                property_dict[prop_name] = 'object'
            # Handle arrays
            elif '[]' in normalized_type:
                base_type = normalized_type.replace('[]', '')
                property_dict[prop_name] = f'List<{base_type}>'
            # Default case
            else:
                property_dict[prop_name] = normalized_type
        
        return class_name, property_dict

# Java controller parser interface
class JavaControllerParser(abc.ABC):
    @abc.abstractmethod
    def parse_controller(self, file_content: str, classifier: EndpointClassifierStrategy) -> Tuple[str, str, List[Dict[str, Any]]]:
        """Parse a Java controller file and extract endpoints."""
        pass

# Concrete Java controller parser
class StandardJavaControllerParser(JavaControllerParser):
    def parse_controller(self, file_content: str, classifier: EndpointClassifierStrategy) -> Tuple[str, str, List[Dict[str, Any]]]:
        """Parse a Java controller file using regex patterns."""
        class_name = re.search(r'class (\w+)', file_content).group(1)
        base_path_match = re.search(r'@RequestMapping(?:\(value\s*=\s*)?\(?"(.+?)"\)?', file_content)
        base_path = base_path_match.group(1) if base_path_match else ''
        
        # Extract entity name from controller name (e.g., ContactController -> Contact)
        entity_name = class_name.replace('Controller', '')
        
        endpoints = []
        # Improved regex to capture more mapping patterns including method attributes
        for method in re.finditer(r'@(\w+Mapping)(?:\((?:value\s*=\s*)?"(.+?)"(?:,\s*method\s*=\s*RequestMethod\.([A-Z]+))?\))?\s+(?:@[^\n]+\s+)*public\s+(?:ResponseEntity<)?([^>]+?)(?:>)?\s+(\w+)\(([^)]*)\)', file_content, re.DOTALL):
            http_method = method.group(1).replace('Mapping', '').lower()
            if http_method == 'request':
                continue  # Skip @RequestMapping annotations
            
            # If method is specified in the annotation, use that instead
            if method.group(3):
                http_method = method.group(3).lower()
            
            path = method.group(2) or ''
            return_type = method.group(4).strip()
            method_name = method.group(5)
            parameters = method.group(6)
            
            # Get endpoint classification
            endpoint_info = classifier.classify(method_name, http_method)
            
            # Create endpoint object with all necessary information
            endpoint = {
                'method': http_method,
                'path': path,
                'name': method_name,
                'parameters': parameters,
                'return_type': return_type,
                **endpoint_info  # Unpack the endpoint info dictionary
            }
            
            endpoints.append(endpoint)
        
        return class_name, base_path, endpoints

# Return type handler interface
class ReturnTypeHandler(abc.ABC):
    @abc.abstractmethod
    def handle_return_type(self, return_type: str, openapi: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a return type and generate the appropriate OpenAPI schema."""
        pass

# Concrete return type handler
class StandardReturnTypeHandler(ReturnTypeHandler):
    def handle_return_type(self, return_type: str, openapi: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a return type using regex patterns."""
        # Default schema
        return_schema = {"type": "object"}
        
        # Handle GlobalResponseMessage
        if "GlobalResponseMessage" in return_type:
            return_schema = {"$ref": "#/components/schemas/GlobalResponseMessage"}
            
            # Check if it contains a generic type
            generic_match = re.search(r'GlobalResponseMessage<([^>]+)>', return_type)
            if generic_match:
                inner_type = generic_match.group(1).strip()
                
                # Handle collections inside GlobalResponseMessage
                if "List<" in inner_type or "ArrayList<" in inner_type or "Set<" in inner_type:
                    collection_match = re.search(r'(?:List|ArrayList|Set)<([^>]+)>', inner_type)
                    if collection_match:
                        collection_inner_type = collection_match.group(1).strip()
                        # Add data schema for the collection
                        openapi["components"]["schemas"]["GlobalResponseMessage"]["properties"]["data"] = {
                            "type": "array",
                            "items": {"$ref": f"#/components/schemas/{collection_inner_type}"}
                        }
                else:
                    # Add data schema for the single object
                    openapi["components"]["schemas"]["GlobalResponseMessage"]["properties"]["data"] = {
                        "$ref": f"#/components/schemas/{inner_type}"
                    }
        
        # Handle direct collection returns
        elif "List<" in return_type or "ArrayList<" in return_type or "Set<" in return_type:
            collection_match = re.search(r'(?:List|ArrayList|Set)<([^>]+)>', return_type)
            if collection_match:
                inner_type = collection_match.group(1).strip()
                return_schema = {
                    "type": "array",
                    "items": {"$ref": f"#/components/schemas/{inner_type}"}
                }
        
        # Handle Page returns
        elif "Page<" in return_type:
            page_match = re.search(r'Page<([^>]+)>', return_type)
            if page_match:
                inner_type = page_match.group(1).strip()
                return_schema = {
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "array",
                            "items": {"$ref": f"#/components/schemas/{inner_type}"}
                        },
                        "pageable": {"type": "object"},
                        "totalElements": {"type": "integer"},
                        "totalPages": {"type": "integer"},
                        "last": {"type": "boolean"},
                        "size": {"type": "integer"},
                        "number": {"type": "integer"},
                        "sort": {"type": "object"},
                        "numberOfElements": {"type": "integer"},
                        "first": {"type": "boolean"},
                        "empty": {"type": "boolean"}
                    }
                }
        
        # Handle direct entity returns
        elif return_type in openapi["components"]["schemas"]:
            return_schema = {"$ref": f"#/components/schemas/{return_type}"}
        
        # Handle primitive types
        elif return_type in ["String", "string"]:
            return_schema = {"type": "string"}
        elif return_type in ["Integer", "int", "Long", "long"]:
            return_schema = {"type": "integer"}
        elif return_type in ["Double", "double", "Float", "float", "BigDecimal"]:
            return_schema = {"type": "number"}
        elif return_type in ["Boolean", "boolean"]:
            return_schema = {"type": "boolean"}
        elif return_type in ["void", "Void"]:
            return_schema = {"type": "object"}
        
        return return_schema

# OpenAPI generator class
class OpenAPIGenerator:
    def __init__(self, 
                 classifier: EndpointClassifierStrategy,
                 endpoint_detector: EndpointDetectorStrategy,
                 java_class_parser: JavaClassParser,
                 controller_parser: JavaControllerParser,
                 parameter_parser: ParameterParser,
                 return_type_handler: ReturnTypeHandler,
                 type_converter: JavaTypeConverter):
        self.classifier = classifier
        self.endpoint_detector = endpoint_detector
        self.java_class_parser = java_class_parser
        self.controller_parser = controller_parser
        self.parameter_parser = parameter_parser
        self.return_type_handler = return_type_handler
        self.type_converter = type_converter
    
    def generate_openapi_contract(self, controller_path: str, request_path: str, response_path: str, output_path: str) -> None:
        """Generate an OpenAPI contract from Java files."""
        with open(controller_path, 'r') as file:
            controller_content = file.read()
        
        class_name, base_path, endpoints = self.controller_parser.parse_controller(controller_content, self.classifier)
        
        # Apply endpoint detector to find missing endpoints
        endpoints = self.endpoint_detector.detect_missing_endpoints(endpoints, class_name.replace('Controller', ''))
        
        # Extract entity name from controller name
        entity_name = class_name.replace('Controller', '')
        
        openapi = {
            "openapi": "3.0.0",
            "info": {
                "title": f"{entity_name} API",
                "version": "1.0.0",
                "description": f"API for {entity_name} operations"
            },
            "paths": {},
            "components": {
                "schemas": {
                    "GlobalResponseMessage": {
                        "type": "object",
                        "properties": {
                            "statusCode": {"type": "integer"},
                            "status": {"type": "string"},
                            "timestamp": {"type": "string", "format": "date-time"},
                            "title": {"type": "string"},
                            "message": {"type": "object"},
                            "description": {"type": "object"},
                            "isError": {"type": "boolean"},
                            "data": {"type": "object"}
                        }
                    }
                }
            }
        }
        
        # Parse Request and Response files if they exist
        if os.path.exists(request_path):
            with open(request_path, 'r') as file:
                request_content = file.read()
            request_class, request_properties = self.java_class_parser.parse_file(request_content)
            openapi["components"]["schemas"][request_class] = {
                "type": "object",
                "properties": {
                    prop: self.type_converter.to_openapi_type(type)
                    for prop, type in request_properties.items()
                }
            }
        
        if os.path.exists(response_path):
            with open(response_path, 'r') as file:
                response_content = file.read()
            response_class, response_properties = self.java_class_parser.parse_file(response_content)
            openapi["components"]["schemas"][response_class] = {
                "type": "object",
                "properties": {
                    prop: self.type_converter.to_openapi_type(type)
                    for prop, type in response_properties.items()
                }
            }
        
        for endpoint in endpoints:
            full_path = f"{base_path}{endpoint['path']}"
            if full_path not in openapi["paths"]:
                openapi["paths"][full_path] = {}
            
            # Handle different return types
            return_schema = self.return_type_handler.handle_return_type(endpoint['return_type'], openapi)
            
            openapi["paths"][full_path][endpoint['method']] = {
                "summary": f"{endpoint['name']}",
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "content": {
                            "application/json": {
                                "schema": return_schema
                            }
                        }
                    }
                }
            }
            
            if endpoint['parameters']:
                openapi["paths"][full_path][endpoint['method']]["parameters"] = []
                for param in endpoint['parameters'].split(','):
                    param_type, param_name, data_type = self.parameter_parser.parse(param)
                    if param_type == 'path':
                        openapi["paths"][full_path][endpoint['method']]["parameters"].append({
                            "name": param_name,
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": data_type
                            }
                        })
                    elif param_type == 'body':
                        # Use the entity name for the request body reference
                        openapi["paths"][full_path][endpoint['method']]["requestBody"] = {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": f"#/components/schemas/{entity_name}Request"
                                    }
                                }
                            }
                        }
                    elif param_type == 'query':
                        openapi["paths"][full_path][endpoint['method']]["parameters"].append({
                            "name": param_name,
                            "in": "query",
                            "schema": {
                                "type": data_type
                            }
                        })
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as yaml_file:
            yaml.dump(openapi, yaml_file, default_flow_style=False)
        
        print(f"OpenAPI contract generated: {output_path}")

def process_directory(root_dir: str) -> None:
    """Process a directory and generate OpenAPI contracts for all controllers."""
    # Create instances of all required components
    classifier = RegexEndpointClassifier()
    endpoint_detector = StandardRESTEndpointDetector(classifier)
    java_class_parser = StandardJavaClassParser()
    controller_parser = StandardJavaControllerParser()
    parameter_parser = RegexParameterParser()
    return_type_handler = StandardReturnTypeHandler()
    type_converter = StandardJavaTypeConverter()
    
    # Create the OpenAPI generator
    generator = OpenAPIGenerator(
        classifier=classifier,
        endpoint_detector=endpoint_detector,
        java_class_parser=java_class_parser,
        controller_parser=controller_parser,
        parameter_parser=parameter_parser,
        return_type_handler=return_type_handler,
        type_converter=type_converter
    )
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('Controller.java'):
                entity = filename[:-15]  # Remove 'Controller.java'
                controller_path = os.path.join(dirpath, filename)
                request_path = os.path.join(dirpath, f"{entity}Request.java")
                response_path = os.path.join(dirpath, f"{entity}Response.java")
                
                relative_path = os.path.relpath(dirpath, root_dir)
                output_path = os.path.join('api_contracts', relative_path, f"{entity}_api.yaml")
                
                generator.generate_openapi_contract(controller_path, request_path, response_path, output_path)

if __name__ == "__main__":
    # Default to src/main/java if no input is provided
    root_dir = "src/main/java"
    print(f"API contract dosyaları oluşturuluyor... Kök dizin: {root_dir}")
    if os.path.exists(root_dir):
        process_directory(root_dir)
        print("API contract dosyaları başarıyla oluşturuldu.")
    else:
        print("Belirtilen dizin bulunamadı.")
