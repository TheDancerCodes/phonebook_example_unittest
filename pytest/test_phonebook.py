
def test_add_and_lookp_entry():
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")
