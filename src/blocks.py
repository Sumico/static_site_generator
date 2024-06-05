import re

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
