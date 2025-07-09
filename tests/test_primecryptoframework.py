# tests/test_primecryptoframework.py
"""
Unit tests for PrimeCryptoFramework.
"""

import unittest
from primecryptoframework import core, utils
import os
import tempfile
import json
import logging

class TestCore(unittest.TestCase):
    """Tests for core module."""
    
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)
        
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, 'test.json')
        with open(self.test_file, 'w') as f:
            json.dump({"Test": "Value"}, f)
            
    def test_processor(self):
        """Test basic processor functionality."""
        output_file = os.path.join(self.temp_dir, 'output.json')
        processor = core.Processor(
            input_path=self.test_file,
            output_path=output_file
        )
        self.assertTrue(processor.execute())
        self.assertTrue(os.path.exists(output_file))
        
    def test_validation(self):
        """Test input validation."""
        processor = core.Processor(input_path="nonexistent.file")
        self.assertFalse(processor.execute())
        
    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

class TestUtils(unittest.TestCase):
    """Tests for utils module."""
    
    def test_transform(self):
        """Test data transformation."""
        data = {"TestKey": "TestValue"}
        transformed = utils.transform(data)
        self.assertEqual(transformed, {"testkey": "testvalue"})
        
    def test_email_validation(self):
        """Test email validation."""
        self.assertTrue(utils.validate_email("test@example.com"))
        self.assertFalse(utils.validate_email("invalid-email"))

if __name__ == "__main__":
    unittest.main()
