# test_hypercode.py
"""
Tests for HyperCode module.
"""

import unittest
from hypercode import HyperCode

class TestHyperCode(unittest.TestCase):
    """Test cases for HyperCode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperCode()
        self.assertIsInstance(instance, HyperCode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperCode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
