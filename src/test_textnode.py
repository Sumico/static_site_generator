import unittest

from textnode import TextNode, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_italic(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", "italic", None)
        self.assertEqual(node, node2)

    def test_properties(self):
        node = TextNode("This is a text node", "italic", "https://url.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "italic")
        self.assertEqual(node.url, "https://url.com")

    """
    def test_split_nodes_delimiter_italic(self):
        nodes = [
            TextNode("This is some text", "text"),
            TextNode("This is **bold** text", "text"),
            TextNode("This is *italic* text", "text"),
            TextNode("This is `code` text", "text"),
            TextNode("This is a [link](https://url.com)", "text"),
            TextNode("This is an image: ![alt text](https://image.com)", "text"),
        ]
        delimiter = "*"
        text_type = "italic"
        expected_nodes = [
            TextNode("This is some text", "text"),
            TextNode("This is **bold** text", "text"),
            TextNode("This is ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text"),
            TextNode("This is `code` text", "text"),
            TextNode("This is a [link](https://url.com)", "text"),
            TextNode("This is an image: ![alt text](https://image.com)", "text"),
        ]
        result_nodes = split_nodes_delimiter(nodes, delimiter, text_type)
        self.assertEqual(result_nodes, expected_nodes)
    """

    def test_split_nodes_delimiter_italic_on_non_italic_textnode(self):
        # Arrange
        nodes = [
            TextNode("This is some text", "text"),
            TextNode("This is **bold** text", "text"),
        ]
        # Act
        actual_nodes = split_nodes_delimiter(nodes, "*", "italic")
        print(actual_nodes)
        expected_nodes = [
            TextNode("This is some text", "text"),
            TextNode("This is **bold** text", "text"),
        ]
        # Assert
        self.assertEqual(actual_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
