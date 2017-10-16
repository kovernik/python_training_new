from model.contact import Contact
import pytest
from data.add_contact import constant as testdata



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", email="", mobilephone="")] + [
    Contact(firstname=random_string("Name", 10), lastname=random_string("Last name", 10),
            email=random_string("kovernik@softbalance.ru", 10), mobilephone=random_string("+79110000000", 10))
    for i in range(3)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
