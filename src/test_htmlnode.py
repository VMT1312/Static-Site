import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", 'text inside a paragraph', ['a', 'b'], {'href':'https://www.google.com'})
        self.assertNotEqual(node.props_to_html(), "")

    def test_single_props(self):
        node = HTMLNode("p", 'text inside a paragraph', ['a', 'b'], {'href':'https://www.google.com'})
        self.assertEqual(node.props_to_html(), ' href=https://www.google.com')

    def test_repr(self):
        node = HTMLNode("p", 'text inside a paragraph', ['a', 'b'], {'href':'https://www.google.com'})
        self.assertEqual(
            "HTMLNode(p, text inside a paragraph, ['a', 'b'], {'href': 'https://www.google.com'})", repr(node)
        )

    def test_child_no_props(self):
        node = LeafNode("p", "This is a paragraph of text")
        self.assertNotEqual(node.to_html(), "This is a paragraph of text")

    def test_child_props(self):
        node = LeafNode("a", "Link", {'href': 'https://www.google.com'})
        self.assertEqual(node.to_html(), '<a href=https://www.google.com>Link</a>')

    def test_child_no_tags(self):
        node = LeafNode(value="This is a paragraph of text")
        self.assertEqual(node.to_html(), "This is a paragraph of text")

    def test_parent_no_props(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")])
        self.assertEqual("<p><b>Bold text</b>Normal text</p>", node.to_html())

    def test_parent_parent(self):
        node = ParentNode("p", 
                          [
            LeafNode("b", "Bold text"), 
            ParentNode("p", [
                LeafNode('a', 'Link', {'href': 'https://www.google.com'})
                ]
                )
                ]
                )
        self.assertEqual("<p><b>Bold text</b><p><a href=https://www.google.com>Link</a></p></p>", node.to_html())


if __name__ == "__main__":
    unittest.main()
