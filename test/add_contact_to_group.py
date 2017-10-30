from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact_to_group(app):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="New_group"))
    new_groups = db.get_group_list()
    group = random.choice(new_groups)
    contact_nig = db.get_contacts_not_in_group(group)
    if len(contact_nig) == 0:
        app.contact.create(Contact(firstname="Mikhail", lastname="Kovernik", mobilephone="79999999999"))
    new_contact = db.get_contacts_not_in_group(group)
    contact = random.choice(new_contact)
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    old_contacts_in_group.append(contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
