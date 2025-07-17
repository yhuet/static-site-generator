import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_em(self):
        node = LeafNode("em", "Emphasis")
        self.assertEqual(node.to_html(), "<em>Emphasis</em>")

    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "Strong")
        self.assertEqual(node.to_html(), "<strong>Strong</strong>")
