import unittest

from markdown_blocks import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_whitespace(self):
        md = """
Whitespace        



Extra newline



            

And some content:

Paragraph
Paragraph continued

    Leading whitespace
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
            [
                "Whitespace",
                "Extra newline",
                "And some content:",
                "Paragraph\nParagraph continued",
                "Leading whitespace",
            ])
