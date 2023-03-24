"""
import necessary module
"""
import unittest
import cap_text


class TestCap(unittest.TestCase):
    '''Capitalize the first letter of a string and return the result.'''

    def test_text_word(self):
        """
        Args:
        text (str): The string to capitalize.
        Returns:
        str: The capitalized string.
        """

        text = "python"
        result = cap_text.cap(text)
        self.assertEqual(result, "Python")

    def test_text_multi_word(self):
        """
        Args:
        text (str): The multi string to capitalize.
        Returns:
        str: The capitalized string.
        """

        text = "mini python"
        result = cap_text.cap(text)
        self.assertEqual(result, "Mini Python")


if __name__ == "__main__":
    unittest.main()
