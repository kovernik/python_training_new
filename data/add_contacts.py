from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", email="email1"),
    Contact(firstname="firstname2", lastname="lastname2", email="email2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", email="", mobilephone="")] + [
    Contact(firstname=random_string("Name", 10), lastname=random_string("Last name", 10),
            email=random_string("kovernik@softbalance.ru", 10), mobilephone=random_string("+79110000000", 10))
    for i in range(3)]


