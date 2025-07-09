# primecryptoframework/__init__.py
"""
PrimeCryptoFramework - A powerful utility for data processing.
"""

__version__ = "0.1.0"
__author__ = "angeldv"
__license__ = "MIT"

from .core import Processor
from .utils import (
    load_data,
    save_data,
    transform,
    validate_email,
    generate_hash
)
