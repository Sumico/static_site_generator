import unittest

from textnode import TextNode, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_italics(self):
        node = TextNode("This is a text node", "italics")
        node2 = TextNode("This is a text node", "italics")
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", "italics", None)
        node2 = TextNode("This is a text node", "italics", None)
        self.assertEqual(node, node2)

    def test_properties(self):
        node = TextNode("This is a text node", "italics", "https://url.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "italics")
        self.assertEqual(node.url, "https://url.com")

    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("This is some text", "text"),
            TextNode("This is **bold** text", "text"),
            TextNode("This is *italics* text", "text"),
            TextNode("This is `code` text", "text"),
            TextNode("This is a [link](https://url.com)", "text"),
            TextNode("This is an image: ![alt text](https://image.com)", "text"),
        ]
        delimiter = "*"
        text_type = "italics"
        expected_nodes = [
            TextNode("This is some text", "text"),
            TextNode("This is ", "text"),
            TextNode("italics", "italics"),
            TextNode(" text", "text"),
            TextNode("This is **bold** text", "text"),
            TextNode("This is `code` text", "text"),
            TextNode("This is a [link](https://url.com)", "text"),
            TextNode("This is an image: ![alt text](https://image.com)", "text"),
        ]
        result_nodes = split_nodes_delimiter(nodes, delimiter, text_type)
        self.assertEqual(result_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
