# primecryptoframework/utils.py
"""
Utility functions for PrimeCryptoFramework.
"""

import json
import csv
from typing import Any, Dict, List, Union
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_data(file_path: str) -> Union[Dict, List, str]:
    """
    Load data from file (JSON, CSV, or text).
    
    Args:
        file_path: Path to input file
        
    Returns:
        Parsed data or raw text
        
    Raises:
        ValueError: For unsupported file types
        IOError: For file access issues
    """
    if not file_path:
        raise ValueError("No file path provided")
        
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
        
    try:
        with path.open('r', encoding='utf-8') as f:
            if path.suffix.lower() == '.json':
                return json.load(f)
            elif path.suffix.lower() == '.csv':
                return list(csv.DictReader(f))
            else:
                return f.read()
    except Exception as e:
        logger.error("Failed to load data: %s", str(e))
        raise

def transform(data: Any) -> Any:
    """
    Transform input data according to business rules.
    
    Args:
        data: Input data to transform
        
    Returns:
        Transformed data
    """
    if isinstance(data, dict):
        return {k.lower(): str(v).lower() for k, v in data.items()}
    elif isinstance(data, list):
        return [transform(item) for item in data]
    return data

def save_data(data: Any, output_path: str) -> None:
    """
    Save data to file (JSON, CSV, or text).
    
    Args:
        data: Data to save
        output_path: Destination file path
        
    Raises:
        ValueError: For unsupported file types
        IOError: For file access issues
    """
    path = Path(output_path)
    try:
        with path.open('w', encoding='utf-8') as f:
            if path.suffix.lower() == '.json':
                json.dump(data, f, indent=2)
            elif path.suffix.lower() == '.csv':
                if isinstance(data, list) and data:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
                else:
                    raise ValueError("Can only save lists of dicts to CSV")
            else:
                f.write(str(data))
    except Exception as e:
        logger.error("Failed to save data: %s", str(e))
        raise

def validate_email(email: str) -> bool:
    """Validate an email address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def generate_hash(data: str, algorithm: str = 'sha256') -> str:
    """
    Generate hash of input data.
    
    Args:
        data: Input string to hash
        algorithm: Hash algorithm to use
        
    Returns:
        Hexadecimal hash string
    """
    import hashlib
    return hashlib.new(algorithm, data.encode()).hexdigest()
