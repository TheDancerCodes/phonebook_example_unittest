"""This file contains test cases for the phonebook app."""
import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    """Class that contains the test cases."""

    def setUp(self):
        """A Test Fixture method that sets up your testing evironment."""
        self.phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        """Test case that looks up an entry by name."""
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))

    def test_missing_entry_raises_KeyError(self):
        """Test case that raises KeyError for a missng entry."""
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        """Test Case that check that empty phonebook is consistent."""
        self.assertTrue(self.phonebook.is_consistent())
