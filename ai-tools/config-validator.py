# Script to validate infrastructure config files
import sys
import os
import json
import yaml

REQUIRED_KEYS = ["name", "version", "infrastructure"]

def load_config(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    with open(file_path, "r") as f:
        if ext in [".yaml", ".yml"]:
            return yaml.safe_load(f)
        elif ext == ".json":
            return json.load(f)
        else:
            raise ValueError("Unsupported file type: {}".format(ext))

def validate_config(config):
    missing = [key for key in REQUIRED_KEYS if key not in config]
    if missing:
        print(f"Missing required keys: {missing}")
        return False
    print("Config is valid.")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python config-validator.py <config-file>")
        sys.exit(1)
    config_file = sys.argv[1]
    try:
        config = load_config(config_file)
        valid = validate_config(config)
        sys.exit(0 if valid else 2)
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(2)