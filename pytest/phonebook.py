"""This file contains the Phonebook functionality."""
import os

class Phonebook():
    """Phonebook Class."""

    def __init__(self):
        """The constructor for the Phonebook class."""
        self.entries = {}
        self.filename = "phonebook.txt"
        self.file_cache = open(self.filename, "w")

    def add(self, name, number):
        """Method that adds a name and number to the phonebook."""
        self.entries[name] = number

    def lookup(self, name):
        """Method that looks up a name in the phonebook."""
        return self.entries[name]

    def names(self):
        """Method that looks up names in the phonebook."""
        return self.entries.keys()

    def numbers(self):
        """Method that looks up numbers in the phonebook."""
        return self.entries.values()

    def clear(self):
        """Method that closes the created file and removes it."""
        self.entries = {}
        self.file_cache.close()
        os.remove(self.filename)
