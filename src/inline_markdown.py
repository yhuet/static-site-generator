from textnode import TextType, TextNode

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