from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_nodes = []
            splitted = node.text.split(delimiter)
            if len(splitted) % 2 == 0:
                raise Exception(f"Invalid Mardown with delimiter {delimiter}")
            for i in range(len(splitted)):
                if splitted[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(splitted[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(splitted[i], text_type))
            new_nodes.extend(split_nodes)
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        split_nodes = []
        matches = extract_markdown_images(text)
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        for image_alt, image_link in matches:
            splitted = text.split(f"![{image_alt}]({image_link})", 1)
            if len(splitted) != 2:
                raise Exception("Invalid Mardown")
            if splitted[0] != "":
                split_nodes.append(TextNode(splitted[0], TextType.TEXT))
            split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            text = splitted[1]
        if text != "":
            split_nodes.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        split_nodes = []
        matches = extract_markdown_links(text)
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        for link_text, link_url in matches:
            splitted = text.split(f"[{link_text}]({link_url})", 1)
            if len(splitted) != 2:
                raise Exception("Invalid Mardown")
            if splitted[0] != "":
                split_nodes.append(TextNode(splitted[0], TextType.TEXT))
            split_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            text = splitted[1]
        if text != "":
            split_nodes.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes