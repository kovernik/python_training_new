# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Name", lastname="Last name", email="kovernik@softbalance.ru",
                      mobilephone="+79110000000", homephone="+78120001110", workphone="+91121111111",
                      company="SoftBalance", address="Shaumyana, 55", middle="Middle", nickname="nickname")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
