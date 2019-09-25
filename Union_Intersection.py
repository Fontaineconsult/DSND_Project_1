class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


    def return_next_node(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def get_head(self):
        return self.head


class HashMap:

    def __init__(self):
        self.hashmap = dict()

    def check_hash(self, value):
        if value in self.hashmap:
            return True
        else:
            return False

    def add(self, value):
        self.hashmap[value] = value


    def _blr(self):
        print(self.hashmap.items())

def union(llist_1, llist_2):

    node_list_1 = llist_1.get_head()
    node_list_2 = llist_2.get_head()
    hashmap = HashMap()
    union_linked_list = LinkedList()

    while node_list_1:

        current_value = node_list_1.value

        if not hashmap.check_hash(current_value):
            hashmap.add(current_value)
            union_linked_list.append(Node(current_value))

            node_list_1 = node_list_1.return_next_node()
        else:
            node_list_1 = node_list_1.return_next_node()

    while node_list_2:

        current_value = node_list_2.value

        if not hashmap.check_hash(current_value):
            hashmap.add(current_value)
            union_linked_list.append(Node(current_value))

            node_list_2 = node_list_2.return_next_node()
        else:
            node_list_2 = node_list_2.return_next_node()

    return union_linked_list


def intersection(llist_1, llist_2):

    node_list_1 = llist_1.get_head()
    node_list_2 = llist_2.get_head()
    hashmap = HashMap()
    hashmap_intersect = HashMap()
    intersected_linked_list = LinkedList()

    while node_list_1:

        current_value = node_list_1.value
        if not hashmap.check_hash(current_value):
            hashmap.add(current_value)
        node_list_1 = node_list_1.return_next_node()



    while node_list_2:

        current_value = node_list_2.value

        if hashmap.check_hash(current_value):
            if not hashmap_intersect.check_hash(current_value):
                intersected_linked_list.append(Node(current_value))
                hashmap_intersect.add(current_value)

            node_list_2 = node_list_2.return_next_node()
        else:
            node_list_2 = node_list_2.return_next_node()


    return intersected_linked_list



def test_case(list_1, list_2):

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()


    for i in list_1:
        linked_list_1.append(i)

    for i in list_2:
        linked_list_2.append(i)


    print("The Union of ", element_1, " and ", element_2, " is ")
    print(str(union(linked_list_1,linked_list_2)))

    print("\n")

    print("The intersection of ", element_1, " and ", element_2, " is ")
    print(str(intersection(linked_list_1,linked_list_2)))

    print("\n")
    print("\n")

if __name__ == '__main__':


    element_1 = [1 , 2, 3, 4, 5, 8, 9]
    element_2 = [1, 2, 3, 4, 5]
    test_case(element_1, element_2)

    element_1 = [24, 1, 23, 6, 33, 4, 4,12,7,4,34,235,7,3,3,12,3,6,587,3,8,35,7,3,457,7]
    element_2 = [7,67,3,2,6,69,78,4,32,1,23,547,76,4,4,8,0,3,2,5,33,35,547,9,67]
    test_case(element_1, element_2)

    element_1 = ['a','b','c']
    element_2 = ['a','b','c','d']
    test_case(element_1, element_2)

    element_1 = []
    element_2 = [10,9,8,7]
    test_case(element_1, element_2)

    element_1 = []
    element_2 = []
    test_case(element_1, element_2)

    element_1 = [1,2,3,4,5,6]
    element_2 = [7,8,9,10,11]
    test_case(element_1, element_2)