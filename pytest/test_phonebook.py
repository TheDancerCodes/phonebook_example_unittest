"""This file contains test cases for the phonebook app."""

from phonebook import Phonebook

def test_add_and_lookp_entry():
    """Test case that adds entry to phonebook & looks up an entry by name."""
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")

# def test_phonebook_gives_access_to_names_and_numbers():
#     """Test case checking that you can access names & numbers in phonebook."""
#     phonebook = Phonebook()
#     phonebook.add("Alice", "12345")
#     assert "Alice" in phonebook.names()
#     assert "12345" in phonebook.numbers()

# Checking two collections and comparing them against each other.
def test_phonebook_gives_access_to_names_and_numbers():
    """Test case checking that you can access names & numbers in phonebook."""
    phonebook = Phonebook()
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    assert set(phonebook.names()) == {"Alice", "Bob"}
    assert set(phonebook.numbers()) == {"12345", "123"}
