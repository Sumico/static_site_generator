import unittest

from textnode import (
    TextNode,
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


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


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_links_empty_text(self):
        text = ""
        link_nodes = extract_markdown_links(text)
        self.assertEqual(len(link_nodes), 0)

    def test_extract_markdown_links_no_links(self):
        text = "This is a plain text without any links."
        link_nodes = extract_markdown_links(text)
        self.assertEqual(len(link_nodes), 0)

    def test_extract_markdown_links_single_link(self):
        text = "This is a [link](https://example.com) to a website."
        link_nodes = extract_markdown_links(text)
        self.assertEqual(len(link_nodes), 1)
        self.assertEqual(link_nodes[0].text, "link")
        self.assertEqual(link_nodes[0].text_type, "link")
        self.assertEqual(link_nodes[0].url, "https://example.com")

    def test_extract_markdown_links_multiple_links(self):
        text = "This is a [link](https://example.com) and another [link](https://example2.com)."
        link_nodes = extract_markdown_links(text)
        self.assertEqual(len(link_nodes), 2)
        self.assertEqual(link_nodes[0].text, "link")
        self.assertEqual(link_nodes[0].text_type, "link")
        self.assertEqual(link_nodes[0].url, "https://example.com")
        self.assertEqual(link_nodes[1].text, "link")
        self.assertEqual(link_nodes[1].text_type, "link")
        self.assertEqual(link_nodes[1].url, "https://example2.com")

    def test_extract_markdown_images_empty_text(self):
        text = ""
        image_nodes = extract_markdown_images(text)
        self.assertEqual(len(image_nodes), 0)

    def test_extract_markdown_images_no_images(self):
        text = "This is a plain text without any images."
        image_nodes = extract_markdown_images(text)
        self.assertEqual(len(image_nodes), 0)

    def test_extract_markdown_images_single_image(self):
        text = "This is an ![image](https://example.com/image.png)."
        image_nodes = extract_markdown_images(text)
        self.assertEqual(len(image_nodes), 1)
        self.assertEqual(image_nodes[0].text, "image")
        self.assertEqual(image_nodes[0].text_type, text_type_image)
        self.assertEqual(image_nodes[0].url, "https://example.com/image.png")

    def test_extract_markdown_images_multiple_images(self):
        text = "This is an ![image1](https://example.com/image1.png) and another ![image2](https://example.com/image2.png)."
        image_nodes = extract_markdown_images(text)
        self.assertEqual(len(image_nodes), 2)
        self.assertEqual(image_nodes[0].text, "image1")
        self.assertEqual(image_nodes[0].text_type, text_type_image)
        self.assertEqual(image_nodes[0].url, "https://example.com/image1.png")
        self.assertEqual(image_nodes[1].text, "image2")
        self.assertEqual(image_nodes[1].text_type, text_type_image)
        self.assertEqual(image_nodes[1].url, "https://example.com/image2.png")

    def test_split_nodes_image_empty_text(self):
        node = TextNode("", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [node])

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is a plain text without any images.", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [node])

    def test_split_nodes_image_single_image(self):
        node = TextNode(
            "This is text with an ![image](https://example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://example.com/image.png"),
            ],
        )

    def test_split_nodes_image_multiple_images(self):
        node = TextNode(
            "This is text with an ![image1](https://example.com/image1.png) and another ![image2](https://example.com/image2.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image1", text_type_image, "https://example.com/image1.png"),
                TextNode(" and another ", text_type_text),
                TextNode("image2", text_type_image, "https://example.com/image2.png"),
            ],
        )

    def test_split_nodes_link_empty_text(self):
        node = TextNode("", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [node])

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is a plain text without any links.", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [node])

    def test_split_nodes_link_single_link(self):
        node = TextNode(
            "This is a [link](https://example.com) to a website.",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a ", text_type_text),
                TextNode("link", text_type_link, "https://example.com"),
                TextNode(" to a website.", text_type_text),
            ],
        )

    def test_split_nodes_link_multiple_links(self):
        node = TextNode(
            "This is a [link1](https://example.com) and another [link2](https://example2.com).",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a ", text_type_text),
                TextNode("link1", text_type_link, "https://example.com"),
                TextNode(" and another ", text_type_text),
                TextNode("link2", text_type_link, "https://example2.com"),
                TextNode(".", text_type_text),
            ],
        )


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected_output = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode(
                "image",
                text_type_image,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(text), expected_output)


if __name__ == "__main__":
    unittest.main()
