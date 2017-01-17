"""This file contains test cases for the phonebook app."""
import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    """Class that contains the test cases."""

    def test_create_phonebook(self):
        """Test Case that creates the phonebook."""
        phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        """Test case that looks up an entry by name."""
        phonebook = Phonebook()
        phonebook.add("Bob", "12345")
        self.assertEqual("12345", phonebook.lookup("Bob"))

    def test_missing_entry_raises_KeyError(self):
        """Test case that raises KeyError for a missng entry."""
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")
