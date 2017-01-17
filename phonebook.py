"""This file contains the Phonebook functionality."""

class Phonebook:
    """Phonebook Class."""

    def __init__(self):
        """The constructor for the Phonebook class."""
        self.entries = {}

    def add(self, name, number):
        """Method that adds a name and number to the phonebook."""
        self.entries[name] = number


    def lookup(self, name):
        """Method that looks up a name in the phonebook."""
        return self.entries[name]
