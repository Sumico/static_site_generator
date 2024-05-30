import unittest

from textnode import TextNode


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
if __name__ == "__main__":
    unittest.main()
