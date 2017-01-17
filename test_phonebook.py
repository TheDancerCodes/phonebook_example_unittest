"""This file contains test cases for the phonebook app."""
import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    """Class that contains the test cases."""

    def test_create_phonebook(self):
        """Test Case that creates the phonebook."""
        phonebook = Phonebook()
