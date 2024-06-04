import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

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

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode('div', None, None)
            node.to_html()

    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, None, [LeafNode('p', 'Hello')])
            node.to_html()

    def test_parent_node_with_one_leaf_child(self):
        node = ParentNode('div', None, [LeafNode('p', 'Hello')])
        self.assertEqual(node.to_html(), '<div><p>Hello</p></div>')

    def test_parent_node_with_multiple_leaf_children(self):
        node = ParentNode('div', None, [LeafNode('p', 'Hello'), LeafNode('p', 'World')])
        self.assertEqual(node.to_html(), '<div><p>Hello</p><p>World</p></div>')

    def test_parent_node_with_one_parent_child(self):
        node = ParentNode('div', None, [ParentNode('p', None, [LeafNode('span', 'Hello')])])
        self.assertEqual(node.to_html(), '<div><p><span>Hello</span></p></div>')

    def test_parent_node_with_multiple_parent_children(self):
        node = ParentNode('div', None, [ParentNode('p', None, [LeafNode('span', 'Hello')]), ParentNode('p', None, [LeafNode('span', 'World')])])
        self.assertEqual(node.to_html(), '<div><p><span>Hello</span></p><p><span>World</span></p></div>')

    def test_parent_node_with_mixed_children(self):
        node = ParentNode('div', None, [LeafNode('p', 'Hello'), ParentNode('div', None, [LeafNode('span', 'World')])])
        self.assertEqual(node.to_html(), '<div><p>Hello</p><div><span>World</span></div></div>')

if __name__ == '__main__':
    unittest.main()