from model.group import Group
from random import randrange


def test_any_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    del old_groups[index]
    assert old_groups == new_groups
