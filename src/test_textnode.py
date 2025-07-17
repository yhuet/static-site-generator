import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is an image", TextType.IMAGE, "/img/test.png")
        node2 = TextNode("This is an image", TextType.IMAGE, "/img/test.png")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is an link", TextType.LINK)
        node2 = TextNode("This is an link", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_ne2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is also a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()