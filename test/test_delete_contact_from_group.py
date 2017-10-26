from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_delete_contact_from_group(app, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Name", lastname="Last name", email="kovernik@softbalance.ru", mobilephone="+79110000000",
                    homephone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                    nickname="nickname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(old_groups)
    old_contacts = db.get_contacts_in_group(Group(id='%s' % group))
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                   key=Contact.id_or_max)
