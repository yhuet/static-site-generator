def markdown_to_blocks(markdown):
    blocks = []
    splitted = markdown.split("\n\n")
    for s in splitted:
        s = s.strip()
        if s != "":
            blocks.append(s)
    return blocks