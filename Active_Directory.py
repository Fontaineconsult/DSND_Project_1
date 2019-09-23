class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):

    if user in group.users:  # Handles user being in parent
        return True

    if not group.get_groups():  # Handles parent having no subgroups.
        return False

    def _walk_group_list(group):

        for item in group.get_groups():

            if user in item.get_users():
                return True
            else:
                if item.get_groups():
                    return _walk_group_list(item)

                else:
                    return False

    return _walk_group_list(group)


if __name__ == '__main__':

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("Is ", sub_child_user, "in Parent :", is_user_in_group(sub_child_user, parent))
    print("Is ChubWump ", "in Parent :", is_user_in_group("ChubWump", parent))


    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_sub_child = Group("subsubchild")
    sub_sub_sub_child = Group("subsubsubchild")
    sub_sub_sub_sub_child = Group("subsubsubsubchild")

    sub_sub_sub_sub_child_user = "YoYOMa"
    sub_sub_sub_sub_child.add_user(sub_sub_sub_sub_child_user)

    sub_sub_sub_child.add_group(sub_sub_sub_sub_child)
    sub_sub_child.add_group(sub_sub_sub_child)
    sub_child.add_group(sub_sub_child)
    child.add_group(sub_child)
    parent.add_group(child)

    print("Is ", sub_sub_sub_sub_child_user, "in Parent :", is_user_in_group(sub_sub_sub_sub_child_user, parent))
    print("Is ChubWump ", "in Parent :", is_user_in_group("ChubWump", parent))


    parent_1 = Group("parent")
    parent_user = "PARENT USER"
    parent_1.add_user(parent_user)

    print("Is ", parent_user, "in Parent :", is_user_in_group(parent_user, parent_1))
    print("Is ChubWump ", "in Parent :", is_user_in_group("ChubWump", parent_1))


