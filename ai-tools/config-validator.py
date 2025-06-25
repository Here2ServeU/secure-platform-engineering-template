# Enhanced Config Validator with HCL support and file-type-specific validation
import sys
import os
import json
import yaml

REQUIRED_KEYS = ["name", "version", "infrastructure"]
REQUIRED_TF_BLOCKS = ["provider", "resource"]

def load_config(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    with open(file_path, "r") as f:
        if ext in [".yaml", ".yml"]:
            return yaml.safe_load(f), ext
        elif ext == ".json":
            return json.load(f), ext
        elif ext == ".tf":
            try:
                import hcl2
            except ImportError:
                raise ImportError("Missing required module 'hcl2'. Install with: pip install python-hcl2")
            return hcl2.load(f), ext
        else:
            raise ValueError(f"Unsupported file type: {ext}")

def validate_config(config, file_type):
    if isinstance(config, list) and len(config) == 1:
        config = config[0]

    if file_type == ".tf":
        present_blocks = list(config.keys())
        missing = [block for block in REQUIRED_TF_BLOCKS if block not in present_blocks]
        if missing:
            print(f"Missing required Terraform blocks: {missing}")
            return False
        print("Terraform configuration is valid.")
        return True
    else:
        missing = [key for key in REQUIRED_KEYS if key not in config]
        if missing:
            print(f"Missing required keys: {missing}")
            return False
        print("Configuration is valid.")
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python config-validator.py <config-file>")
        sys.exit(1)

    config_file = sys.argv[1]
    try:
        config, file_type = load_config(config_file)
        valid = validate_config(config, file_type)
        sys.exit(0 if valid else 2)
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(2)
