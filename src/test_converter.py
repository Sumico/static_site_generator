import unittest
from utils.convert import text_node_to_html_node
from textnode import TextNode


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_bold(self):
        node = TextNode("Hello, world!", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Hello, world!")

    def test_text_node_to_html_node_text(self):
        node = TextNode("Hello, world!", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello, world!")

    def test_text_node_to_html_node_italics(self):
        node = TextNode("Hello, world!", "italics")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Hello, world!")

    def test_text_node_to_html_node_link(self):
        node = TextNode("GitHub", "link", "https://github.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "GitHub")
        self.assertEqual(html_node.props, {"href": "https://github.com"})

    def test_text_node_to_html_node_code(self):
        node = TextNode("print('Hello, world!')", "code")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello, world!')")

    def test_text_node_to_html_node_image(self):
        node = TextNode("GitHub Logo", "image", "https://github.com/logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {"src": "https://github.com/logo.png", "alt": "GitHub Logo"},
        )

    def test_text_node_to_html_node_invalid(self):
        node = TextNode("Hello, world!", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
