import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import (
    TextNode,
    text_node_to_html_node,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_link,
    text_type_code,
    text_type_image,
)

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"
block_type_quote = "quote"
block_type_code = "code"


def markdown_to_blocks(markdown):
    pattern = r"\n\n+"
    result = re.split(pattern, markdown)
    result = [block.strip() for block in result]
    return result


def block_to_block_type(block):
    if block.startswith("#"):
        return block_type_heading
    if block.startswith("* ") or block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("* ") and not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        for i, line in enumerate(block.split("\n")):
            if not line.startswith(f"{i + 1}. "):
                return block_type_paragraph
        return block_type_ordered_list
    if block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    return block_type_paragraph


def paragraph_block_to_html(block):
    return f"<p>{block}</p>"


def heading_block_to_html(block):
    level = 0
    while block[level] == "#":
        level += 1
    return f"<h{level}>{block[level:]}</h{level}>"


def unordered_list_block_to_html(block):
    items = block.split("\n")
    items = [f"<li>{item[2:]}</li>" for item in items]
    items = "".join(items)
    return f"<ul>{items}</ul>"


def ordered_list_block_to_html(block):
    items = block.split("\n")
    items = [f"<li>{item[3:]}</li>" for item in items]
    items = "".join(items)
    return f"<ol>{items}</ol>"


def quote_block_to_html(block):
    lines = block.split("\n")
    lines = [f"<p>{line[2:]}</p>" for line in lines]
    lines = "".join(lines)
    return f"<blockquote>{lines}</blockquote>"


def code_block_to_html(block):
    code = block[3:-3]
    return f"<pre><code>{code}</code></pre>"


def block_to_html(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_block_to_html(block)
    if block_type == block_type_heading:
        return heading_block_to_html(block)
    if block_type == block_type_unordered_list:
        return unordered_list_block_to_html(block)
    if block_type == block_type_ordered_list:
        return ordered_list_block_to_html(block)
    if block_type == block_type_quote:
        return quote_block_to_html(block)
    if block_type == block_type_code:
        return code_block_to_html(block)
    return ""


def document_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = [block_to_html(block) for block in blocks]
    html_nodes = []
    for block in html_blocks:
        nodes = text_to_textnodes(block)
        print(nodes)
        html_nodes.extend([text_node_to_html_node(node) for node in nodes])
    html = "<div>" + "".join([node.to_html() for node in html_nodes]) + "</div>"
    return html
