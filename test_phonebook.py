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

    @unittest.skip("poor example")
    def test_is_consistent(self):
        """Test Case to check that enties are consistent."""
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "12345") # identical to Bob
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "123") # prefix of Bob
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        """Test Case to check that enties are consistent."""
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsostent(self):
        """Test Case to check that duplicate enties are inconsistent."""
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        """Test Case to check that numbers prefixing each other are inconsistent."""
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_add_names_and_numbers(self):
        """Test Case to check the names and numbers the phonebook contains."""
        self.phonebook.add("Sue", "12345")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())
