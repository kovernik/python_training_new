from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact_to_group(app):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="New_group"))
    groups = db.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = db.get_contacts_in_group(group)
    if len(db.get_contact_list()) == 0 or len(db.get_contact_list()) == len(old_contacts_in_group):
        app.contact.fill_new(Contact(firstname="NEWSContact"))
    contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_in_group(contact, group)
    new_contact_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) + 1 == len(new_contact_in_group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contact_in_group, key=Contact.id_or_max)
