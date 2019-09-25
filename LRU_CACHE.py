import random

class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def size(self):
        return self.length

    def get_head(self):
        return self.head

    def set_head(self, node):

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if node.value == self.head.value:  # if the value is the same as the head don't do anything
                return

            self.head.left = node  # set old heads left to new head
            old_head = self.head  # save the current head
            self.head = node  # put the new node at head
            self.head.right = old_head  # set new heads right to old head
            self.head.left = None

    def set_tail(self, node):
        self.tail = node
        self.tail.right = None

    def insert(self, node):

        self.set_head(node)
        self.length += 1

    def move_to_front(self, node):

        self.bind_neighbors(node)
        self.set_head(node)


    def remove_least_used(self):

        tail_node = self.tail
        self.tail = self.tail.left
        self.tail.right = None
        self.length -= 1
        return tail_node.key

    def bind_neighbors(self, node):

        if node.right is not None and node.left is not None:

            left_node = node.left
            right_node = node.right

            left_node.right = right_node
            right_node.left = left_node

        if node.right is None and node.left is not None:

            self.tail = node.left
            self.tail.right = None

        elif node.left is None:

            pass


class HashMap(object):
    def __init__(self):
        self.table = dict()

    def store(self, key, node):
        self.table[key] = node


    def lookup(self, key):

        if key in self.table:

            return self.table[key]
        else:
            return False

    def delete(self, key):
        del self.table[key]


class LRUCache(object):

    def __init__(self, capacity):
        self.cache_list = LinkedList()
        self.hashmap = HashMap()
        self.capacity = capacity
        # Initialize class variables

    def get(self, key):

        lookup_node = self.hashmap.lookup(key)

        if lookup_node is not False:

            self.cache_list.move_to_front(lookup_node)
            return lookup_node.value
        else:
            return -1

        # Retrieve item from provided key. Return -1 if nonexistent.

    def set(self, key, value):

        if self.capacity == 0:
            return "Can't set a 0 capacity cache"

        lookup_node = self.hashmap.lookup(key)

        if lookup_node is not False:

            if lookup_node.value != value:
                lookup_node.value = value

            self.cache_list.move_to_front(lookup_node)
            return lookup_node.value

        else:
            node = Node(key, value)

            if self.cache_list.size() < self.capacity:

                self.hashmap.store(key, node)
                self.cache_list.insert(node)
                return node.value

            else:
                # add node to front and add to dict
                self.hashmap.store(key, node)
                self.cache_list.insert(node)
                # remove node to back and remove from dict

                removed_node_key = self.cache_list.remove_least_used()
                self.hashmap.delete(removed_node_key)
                return node.value

    def __str__(self):

        node = self.cache_list.get_head()
        representation = ''
        for x in range(self.cache_list.size()):

            representation += str(node.value) + " - "
            node = node.right
        return representation

        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.


if __name__ == "__main__":

    our_cache = LRUCache(5)

    values_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print('Test 1: Setting Values')
    for each in values_1:
        our_cache.set(each, each)
        print(our_cache)

    print("Test 1: Getting Values")
    for each in values_1:
        print("Getting Value {} from cache".format(each), "Got Value, {}".format(our_cache.get(each)))
        print(our_cache)
    print("\n")
    values_1_1 = [7, 8, 9, 10]
    print("Test 2: Resetting Values from Test 1")
    for each in values_1_1:
        print("Resetting: {} to {} and got {}".format(each, each + 100, our_cache.set(each, each + 100)))
        print(our_cache)
    print("\n")
    print("Test 3: 0 Length Cache")

    our_cache = LRUCache(0)
    print(our_cache.set(1,1))
    print("Getting Value {} from cache".format(1), "Got Value, {}".format(our_cache.get(1)))
