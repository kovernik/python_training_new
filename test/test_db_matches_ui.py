from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
<<<<<<< HEAD


def test_contacts_from_db_matches_contacts_from_ui(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = db.get_contact_list_db()
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
=======
>>>>>>> 91819225a9449fdbf9dba956285cce47c45f1de2
