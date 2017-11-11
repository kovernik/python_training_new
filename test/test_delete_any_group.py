from model.group import Group
import pytest
import random


def test_delete_any_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New"))
    old_groups = db.get_group_list()
    with pytest.allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with pytest.allure.step('When I delete the group %s from the list' % group):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
