import unittest

from generator import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

* and
* a
* list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass

    
    def test_extract_title(self):
        md = '# Title'
        title = extract_title(md)
        self.assertEqual(
            title,
            'Title'
        )


    def test_no_h1_header(self):
        markdown = "## Subheader\nText without h1"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found in this markdown")


    def test_extract_empty(self):
        markdown = ' \n \n '
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), 'No h1 header found in this markdown')


if __name__ == "__main__":
    unittest.main()

