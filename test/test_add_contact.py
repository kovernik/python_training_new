from model.contact import Contact


<<<<<<< HEAD
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list_db()
    app.contact.create(contact)
    new_contacts = db.get_contact_list_db()
=======
def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
>>>>>>> 91819225a9449fdbf9dba956285cce47c45f1de2
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_db(),
                                                                     key=Contact.id_or_max)
