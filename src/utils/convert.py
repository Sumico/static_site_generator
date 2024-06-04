from htmlnode import LeafNode


def text_node_to_html_node(node):
    if node.text_type == "bold":
        return LeafNode("b", node.text)
    if node.text_type == "text":
        return LeafNode(None, node.text)
    if node.text_type == "italics":
        return LeafNode("i", node.text)
    if node.text_type == "link":
        return LeafNode("a", node.text, {"href": node.url})
    if node.text_type == "code":
        return LeafNode("code", node.text)
    if node.text_type == "image":
        return LeafNode("img", None, {"src": node.url, "alt": node.text})
    raise ValueError("Invalid text type: {node.text_type}")
