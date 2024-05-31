import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node = HTMLNode("a", "valval", "no_children", {"href": "http://example.com", "class": "link"})

    def test_init(self):
        self.assertEqual(self.node.tag, "a")
        self.assertEqual(self.node.value, "valval")
        self.assertEqual(self.node.children, "no_children")
        self.assertEqual(self.node.props, {"href": "http://example.com", "class": "link"})

    def test_repr(self):
        expected_output = """
        tag: a
        value: valval
        children: no_children
        props: {'href': 'http://example.com', 'class': 'link'}
        """
        self.assertEqual(self.node.__repr__(), expected_output)

    def test_props_to_html(self):
        expected_output = "href: http://example.com class: link"
        self.assertEqual(self.node.props_to_html(), expected_output)

if __name__ == '__main__':
    unittest.main()