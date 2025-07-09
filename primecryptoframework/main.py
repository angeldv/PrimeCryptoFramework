# primecryptoframework/main.py
"""
Main entry point for the PrimeCryptoFramework application.
"""

import argparse
import logging
from primecryptoframework import core, utils

def configure_logging(verbose=False):
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='PrimeCryptoFramework - A powerful utility for data processing',
        epilog='Example: python -m primecryptoframework --input data.json --output result.json'
    )
    parser.add_argument('-i', '--input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    configure_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Initializing %s processor", base_name)
        processor = core.Processor(
            input_path=args.input,
            output_path=args.output,
            verbose=args.verbose
        )
        
        result = processor.execute()
        if result:
            logger.info("Operation completed successfully")
        else:
            logger.warning("Operation completed with warnings")
        
        return 0 if result else 1
        
    except Exception as e:
        logger.error("Processing failed: %s", str(e), exc_info=args.verbose)
        return 1

if __name__ == "__main__":
    exit(main())
