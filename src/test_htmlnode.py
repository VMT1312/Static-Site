import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
