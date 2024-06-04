from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italics = "italics"
text_type_link = "link"
text_type_code = "code"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(node):
    if node.text_type == text_type_bold:
        return LeafNode("b", node.text)
    if node.text_type == text_type_text:
        return LeafNode(None, node.text)
    if node.text_type == text_type_italics:
        return LeafNode("i", node.text)
    if node.text_type == text_type_link:
        return LeafNode("a", node.text, {"href": node.url})
    if node.text_type == text_type_code:
        return LeafNode("code", node.text)
    if node.text_type == text_type_image:
        return LeafNode("img", None, {"src": node.url, "alt": node.text})
    raise ValueError("Invalid text type: {node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter in node.text:
            parts = node.text.split(delimiter)
