#import re
#from model.contact import Contact


#def test_emails_on_home_page(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Mikhail"))
#    contact_from_home_page = app.contact.get_contact_list()[0]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_home_page.all_emails_from_home_page == merge_emails_on_home_page(contact_from_edit_page)


#def test_phones_on_contacts_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#    assert contact_from_view_page.fax == contact_from_edit_page.fax
#    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


#def clear(s):
#    return re.sub("[() -],", "", s)


#def merge_emails_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
#                                                                         [contact.email, contact.email2,
#                                                                          contact.email3]))))
