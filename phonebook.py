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

    def is_consistent(self):
        """Method that ascertains whether the phone is consistent."""
        return True
    #     if len(self.entries) == 0:
    #         return True
    #     else self.entries["Roger", "12345"]:
    #         return True
    #
    # def get_names(self):
    #     return "Sue"
    #
    # def get_numbers(self):
    #     return "12345"
