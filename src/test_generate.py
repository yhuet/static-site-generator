import unittest

from generate import extract_title

class TestGenerate(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Title

Some content
"""
        self.assertEqual("Title", extract_title(md))