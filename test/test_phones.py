import re
from model.contact import Contact
from random import randrange


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Mikhail"))
    index = randrange(len(app.contact.get_contact_list_db()))
    contact_from_home_page = app.contact.get_contact_list_db()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -],", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.homephone, contact.workphone,
                                                                               contact.mobilephone,
                                                                               contact.secondaryphone]))))


def merge_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.email, contact.email2,
                                                                               contact.email3]))))
