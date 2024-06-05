import unittest

from blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    block_type_paragraph,
    block_type_unordered_list,
    block_type_ordered_list,
    block_type_quote,
    block_type_code,
)


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown_text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is a list item\n* This is another list item",
        ]
        self.assertEqual(markdown_to_blocks(markdown_text), expected_blocks)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_type_unordered_list(self):
        block = "* This is a list item\n* This is another list item"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is a list item\n2. This is another list item"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_to_block_type_paragraph_start_with_number(self):
        block = "1. This is a list item\n2. This is another list item\nThis is not a list item"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
