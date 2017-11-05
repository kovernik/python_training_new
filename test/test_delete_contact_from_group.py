from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_del_contact(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    group = random.choice(db.get_group_list())
    if len(db.get_contacts_not_in_group(Group(id=group.id))) == 0:
        app.contact.create(Contact(lastname="lastname", firstname="firstname", address="address", email="email"))
    contact_not_in_group = random.choice(db.get_contacts_not_in_group(Group(id=group.id)))
    app.contact.add_contact_to_group_by_id(contact_not_in_group.id, group.id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    contact_in_group = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group_by_id(contact_in_group.id, group.id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    old_contacts_in_group.remove(contact_in_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
