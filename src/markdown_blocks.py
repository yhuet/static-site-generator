from enum import Enum
from parentnode import ParentNode
from textnode import TextNode, TextType
from inline_markdown import text_to_textnodes
from text_to_html import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    splitted = markdown.split("\n\n")
    for s in splitted:
        s = s.strip()
        if s != "":
            blocks.append(s)
    return blocks

def block_to_block_type(block: str):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def lines_to_list_item(lines):
    items = []
    for line in lines:
        children = text_to_children(line)
        node = ParentNode("li", children)
        items.append(node)
    return items

def block_paragraph(block):
    tag = "p"
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode(tag, children)

def block_heading(block):
    if block.startswith("# "):
        tag = "h1"
        text = block[2:]
    elif block.startswith("## "):
        tag = "h2"
        text = block[3:]
    elif block.startswith("### "):
        tag = "h3"
        text = block[4:]
    elif block.startswith("#### "):
        tag = "h4"
        text = block[5:]
    elif block.startswith("##### "):
        tag = "h5"
        text = block[6:]
    elif block.startswith("###### "):
        tag = "h6"
        text = block[7:]
    children = text_to_children(text)
    return ParentNode(tag, children)

def block_code(block):
    text = block[4:-3]
    text_node = TextNode(text, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    code = ParentNode("code", [html_node])
    return ParentNode("pre", [code])

def block_quote(block):
    tag = "blockquote"
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line[2:])
    text = "\n".join(new_lines)
    children = text_to_children(text)
    return ParentNode(tag, children)

def block_unordered_list(block):
    tag = "ul"
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line[2:])
    children = lines_to_list_item(new_lines)
    return ParentNode(tag, children)

def block_ordered_list(block):
    tag = "ol"
    lines = block.split("\n")
    new_lines = []
    i = 1
    j = 3
    for line in lines:
        if i > 9:
            j = 4 
        new_lines.append(line[j:])
        i += 1
    children = lines_to_list_item(new_lines)
    return ParentNode(tag, children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return block_paragraph(block)
    if block_type == BlockType.HEADING:
        return block_heading(block)
    if block_type == BlockType.CODE:
        return block_code(block)
    if block_type == BlockType.QUOTE:
        return block_quote(block)
    if block_type == BlockType.UNORDERED_LIST:
        return block_unordered_list(block)
    if block_type == BlockType.ORDERED_LIST:
        return block_ordered_list(block)



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        node = block_to_html_node(block)
        children.append(node)
    return ParentNode("div", children)