import json

# Method shall return logical false if an input JSON Resource field contains a single asterisk and true in any other case.
def validate_json(json_file) -> bool:
    try:
        content = json.loads(json_file)
        resource_value = content.get("Resource")
        if isinstance(resource_value,str) and resource_value.strip() == '*':
            return True
        return False
    except json.JSONDecodeError:
        print("Invalid JSON Format")
        return False

json_data = '{"resource": "*", "field2": "value2", "field3": "*" }'
print(validate_json(json_data))