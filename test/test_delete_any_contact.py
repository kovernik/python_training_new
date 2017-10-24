from model.contact import Contact
import random


def test_delete_any_contact(app, db):
    if len(db.get_contact_list_db()) == 0:
        app.contact.create(
            Contact(firstname="Name", lastname="Last name", email="kovernik@softbalance.ru", mobilephone="+79110000000",
                    homephone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                    nickname="nickname"))
    old_contacts = db.get_contact_list_db()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list_db()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
