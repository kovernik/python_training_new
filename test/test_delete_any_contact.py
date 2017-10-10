from model.contact import Contact
from random import randrange


def test_delete_any_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Name", lastname="Last name", email="kovernik@softbalance.ru", mobilephone="+79110000000",
                    homephone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                    nickname="nickname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    del old_contacts[index]
    assert old_contacts == new_contacts
