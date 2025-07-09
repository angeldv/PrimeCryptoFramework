# primecryptoframework/core.py
"""
Core processing logic for PrimeCryptoFramework.
"""

import os
import logging
from typing import Optional, Any, Dict, List, Union
from pathlib import Path
from . import utils

class Processor:
    """Main processor class for PrimeCryptoFramework operations."""
    
    def __init__(self, input_path: Optional[str] = None,
                 output_path: Optional[str] = None,
                 verbose: bool = False):
        """
        Initialize the processor.
        
        Args:
            input_path: Path to input file
            output_path: Path for output file
            verbose: Enable verbose logging
        """
        self.input_path = input_path
        self.output_path = output_path
        self.verbose = verbose
        self.logger = logging.getLogger(__name__)
        
        if verbose:
            self.logger.setLevel(logging.DEBUG)
        
    def validate(self) -> bool:
        """Validate input and output paths."""
        if self.input_path and not Path(self.input_path).exists():
            self.logger.error("Input file does not exist: %s", self.input_path)
            return False
            
        if self.output_path:
            output_dir = Path(self.output_path).parent
            if not output_dir.exists():
                try:
                    output_dir.mkdir(parents=True, exist_ok=True)
                except OSError as e:
                    self.logger.error("Failed to create output directory: %s", str(e))
                    return False
                    
        return True
        
    def process(self) -> Any:
        """Execute the main processing logic."""
        self.logger.debug("Starting data processing")
        
        try:
            data = utils.load_data(self.input_path)
            processed = utils.transform(data)
            
            if self.output_path:
                utils.save_data(processed, self.output_path)
                return True
                
            return processed
            
        except Exception as e:
            self.logger.error("Processing error: %s", str(e), exc_info=self.verbose)
            raise
            
    def execute(self) -> Any:
        """Execute the full processing pipeline."""
        if not self.validate():
            return False
            
        return self.process()
