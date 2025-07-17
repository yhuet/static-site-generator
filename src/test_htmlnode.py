import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode, "node creation")

    def test_repr(self):
        node = HTMLNode("p", "This is a test", None, {"class":"red"})
        self.assertEqual(repr(node), "HTMLNode(tag: p, value: This is a test, children: None, props: {'class': 'red'})")

    def test_div(self):
        node = HTMLNode("div")
        self.assertEqual("div", node.tag)

    def test_props(self):
        node = HTMLNode("p", "This is a paragraph.", None, {"class":"blue"})
        self.assertEqual(' class="blue"', node.props_to_html(), "testing props_to_html()")