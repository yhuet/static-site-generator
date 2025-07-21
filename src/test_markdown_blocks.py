import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

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

    def test_block_to_block_type_heading(self):
        block = "# Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\nCode\nBlock\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = ">This\n>is\n>a\n>quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "- Some\n- Items"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. One\n2. Two"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "A simple paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)