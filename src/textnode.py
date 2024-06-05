from htmlnode import LeafNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
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
    if node.text_type == text_type_italic:
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
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def is_image(text):
    return re.match(r"!\[.*?\]\(.*?\)", text) is not None


def is_link(text):
    return re.match(r"\[.*?\]\(.*?\)", text) is not None


def extract_markdown_images(text):
    image_nodes = []
    for match in re.finditer(r"!\[(.*?)\]\((.*?)\)", text):
        image_nodes.append(TextNode(match.group(1), text_type_image, match.group(2)))
    return image_nodes


def extract_markdown_links(text):
    link_nodes = []
    for match in re.finditer(r"\[(.*?)\]\((.*?)\)", text):
        link_nodes.append(TextNode(match.group(1), text_type_link, match.group(2)))
    return link_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    pattern = r"(!\[.*?\]\(.*?\)|[^!]*?(?=\!\[|$))"
    for old_node in old_nodes:
        split_nodes = []
        if old_node.text == "":
            new_nodes.append(old_node)
            continue
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split = re.findall(pattern, old_node.text)
        parts = [part for part in split if part != ""]
        for part in parts:
            if is_image(part):
                image_nodes = extract_markdown_images(part)
                split_nodes.extend(image_nodes)
            else:
                split_nodes.append(TextNode(part, text_type_text))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = r"(\[.*?\]\(.*?\)|[^[]*?(?=\[|$))"
    for old_node in old_nodes:
        split_nodes = []
        if old_node.text == "":
            new_nodes.append(old_node)
            continue
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split = re.findall(pattern, old_node.text)
        parts = [part for part in split if part != ""]
        for part in parts:
            if is_link(part):
                link_nodes = extract_markdown_links(part)
                split_nodes.extend(link_nodes)
            else:
                split_nodes.append(TextNode(part, text_type_text))
        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text):
    text_nodes = [TextNode(text, text_type_text)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", text_type_bold)
    text_nodes = split_nodes_delimiter(text_nodes, "*", text_type_italic)
    text_nodes = split_nodes_delimiter(text_nodes, "`", text_type_code)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
