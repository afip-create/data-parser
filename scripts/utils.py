import os
import json
from typing import Dict, List, Optional, Union
import logging

logger = logging.getLogger(__name__)

def read_json_file(file_path: str) -> Optional[Dict]:
    """Read and parse a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading JSON file {file_path}: {e}")
        return None

def write_json_file(file_path: str, data: Union[Dict, List]) -> bool:
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except (IOError, TypeError) as e:
        logger.error(f"Error writing JSON file {file_path}: {e}")
        return False

def ensure_directory_exists(dir_path: str) -> bool:
    """Ensure a directory exists; create it if not."""
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except OSError as e:
        logger.error(f"Error creating directory {dir_path}: {e}")
        return False

def get_file_extension(file_path: str) -> str:
    """Get the file extension from a file path."""
    _, ext = os.path.splitext(file_path)
    return ext.lower()

def validate_file_path(file_path: str) -> bool:
    """Validate if a file path exists and is a file."""
    return os.path.exists(file_path) and os.path.isfile(file_path)