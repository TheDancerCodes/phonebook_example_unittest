"""This file contains test cases for the phonebook app."""

from phonebook import Phonebook

def test_add_and_lookp_entry():
    """Test case that adds entry to phonebook & looks up an entry by name."""
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")
