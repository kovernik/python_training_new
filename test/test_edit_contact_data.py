from model.contact import Contact
import random


def test_edit_contact_data(app, db, check_ui):
<<<<<<< HEAD
    if len(db.get_contact_list_db()) == 0:
        app.contact.create(Contact(firstname="Mikhail"))
    old_contacts = db.get_contact_list_db()
    contact = Contact(firstname="New_name1")
    contact.id = random.choice(old_contacts).id
    app.contact.edit_contact_by_index(contact.id, contact)
    new_contacts = db.get_contact_list_db()
=======
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Mikhail"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="New_name1")
    contact.id = random.choice(old_contacts).id
    app.contact.edit_contact_by_index(contact.id, contact)
    new_contacts = db.get_contact_list()
>>>>>>> 91819225a9449fdbf9dba956285cce47c45f1de2
    assert len(old_contacts) == len(new_contacts)
    contact.id = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
<<<<<<< HEAD
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_db(),
=======
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
>>>>>>> 91819225a9449fdbf9dba956285cce47c45f1de2
                                                                     key=Contact.id_or_max)
