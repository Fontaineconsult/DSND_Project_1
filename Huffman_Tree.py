from collections import deque


class Node(object):

    def __init__(self, chars, total):
        self.chars = chars
        self.total = total
        self.bit = None
        self.left_child = None
        self.right_child = None

    def get_children(self):
        return [self.left_child, self.right_child]

    def get_bit(self):
        return self.bit, self.chars

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.left_child is not None

    def has_children(self):
        return self.left_child is not None and self.right_child is not None


class State(object):

    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True


class Tree(object):

    def __init__(self, start_nodes):
        self.root = None
        self.start_nodes = start_nodes
        self.root_to_leaf_paths = []

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def bfs_walk(self):
        nodes = []
        stack = [self.get_root()]

        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            nodes.append(cur_node)

            if cur_node is not None:

                for child in cur_node.get_children():
                    if child is not None:
                        stack.append(child)

        return nodes

    def dfs_walk(self):

        node = self.get_root()
        visit_order = list()

        def _dfs_walk(node):
            visit_order_internal = []
            if node:

                _dfs_walk(node.left_child)
                visit_order_internal.append((node.bit, node.chars, node.total))
                _dfs_walk(node.right_child)

            return visit_order_internal
        return _dfs_walk(node)

    def get_root_to_leaf(self):

        #
        # Implemented but not used. Couldn't figure out how to adapt to get all root to leaf paths.
        #

        visit_order = list()
        current_path = []

        paths = []
        stack = deque()
        path_stack = deque()
        node = self.get_root()
        visit_order.append(node.get_bit())
        state = State(node)
        stack.append(state)
        path_stack.append(state)
        count = 0

        while node:
            count += 1
            if node.has_left_child() and not state.get_visited_left():
                state.set_visited_left()
                node = node.get_left_child()
                visit_order.append(node.get_bit())
                state = State(node)
                stack.append(state)
                path_stack.append(state)
            elif node.has_right_child() and not state.get_visited_right():
                state.set_visited_right()
                node = node.get_right_child()
                visit_order.append(node.get_bit())
                state = State(node)
                stack.append(state)
                path_stack.append(state)
            else:

                if not node.has_children():

                    path = []
                    for each in stack:
                        path.append(each.get_node())
                    paths.append(path)

                stack.pop()
                path_stack.pop()

                if not len(stack) == 0:
                        state = stack.pop()
                        node = state.get_node()
                else:
                    node = None
        return paths

    def generate_root_to_leaf_paths(self):

        #
        # Adapted from:
        # https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/
        #

        def generate_paths(root):

            path = []
            _walk_nodes(root, path, 0)

        def _walk_nodes(node, path, pathlen):

            if node is None:
                return

            if len(path) > pathlen:

                path[pathlen] = (node.chars, node.bit)
            else:
                path.append((node.chars, node.bit))

            pathlen = pathlen + 1

            if not node.has_children():

                outputpath(path)

            else:

                _walk_nodes(node.get_left_child(), path, pathlen)
                _walk_nodes(node.get_right_child(), path, pathlen)

        def outputpath(path):

            set = []
            for i in path:
                set.append(i)
            self.root_to_leaf_paths.append(set)

        generate_paths(self.get_root())
        return self.root_to_leaf_paths


def huffman_encoding(data):

    start_nodes = []
    encoding_dict = {}
    encoded_text = ''

    if len(data) == 0:
        print("Empty String")
        return "", None

    def build_count_dict(data):
        char_count = {}

        for each in data:
            if each in char_count:
                char_count[each] += 1
            else:
                char_count[each] = 1

        return char_count

    def insert_in_order(node, list):

        if len(list) == 0:
            return 0
        else:
            for index, item in enumerate(list):
                if item.total < node.total:

                    return index
                else:
                    return 0

    char_dict = build_count_dict(data)

    for each in char_dict.items():
        start_nodes.append(Node(each[0], each[1]))

    if len(start_nodes) == 1:
        # Trick to handle single char strings.
        # adds duplicate to char list so we can create a combo node
        start_nodes.append(start_nodes[0])

    start_nodes.sort(key=lambda node: node.total, reverse=True)

    huffman_tree = Tree(len(start_nodes))

    while len(start_nodes) >= 2:

            first_node = start_nodes.pop()
            second_node = start_nodes.pop()
            combined_value = first_node.total + second_node.total
            combined_chars = first_node.chars + second_node.chars
            combined_node = Node(combined_chars, combined_value)
            combined_node.right_child = second_node
            combined_node.left_child = first_node
            huffman_tree.set_root(combined_node)
            start_nodes.insert(insert_in_order(combined_node, start_nodes), combined_node)

    #  add binary encoding

    add_bit = huffman_tree.bfs_walk()
    bit = 0
    for each in add_bit[1:]:
        each.bit = bit
        bit = 1 if bit == 0 else 0

    # get root to leaf paths for each character
    root_to_leaf = huffman_tree.generate_root_to_leaf_paths()
    print(root_to_leaf)


    for each_path in root_to_leaf:
        #root_to_leaf is a list of lists
        #each_path is a list of tuples. [0] = char, [1] = binary encoding

        bitstring = ''
        key = None
        for each_node in each_path[1:]:
            bitstring += str(each_node[1])
            key = each_node[0]

        encoding_dict[key] = bitstring

    for each_char in data:
        encoded_text += encoding_dict[each_char]

    return encoded_text, huffman_tree


def huffman_decoding(encoding, tree):

    binary = encoding
    text_string = ''

    try:
        node = tree.get_root()
    except AttributeError:
        return None

    for each_bit in binary:
        if node.has_children():
            if each_bit == '0':
                node = node.get_left_child()

                if not node.has_children():

                    text_string += node.chars
                    node = tree.get_root()
            if each_bit == '1':
                node = node.get_right_child()

                if not node.has_children():

                    text_string += node.chars
                    node = tree.get_root()

    return text_string


if __name__ == '__main__':
    a_test_string = "This is a really good test string"
    print("First Test String: ", a_test_string)
    encoded_data, tree = huffman_encoding(a_test_string)
    print("The Huffman Code: ", encoded_data)
    decode = huffman_decoding(encoded_data, tree)
    print("The Decoded String ", decode)

    print("\n")

    another_test_string = "112"
    print("Second Test String: ", another_test_string)
    encoded_data, tree = huffman_encoding(another_test_string)
    print("The Huffman Code: ", encoded_data)
    decode = huffman_decoding(encoded_data, tree)
    print("The Decoded String ", decode)

    print("\n")

    last_test_string = "A"
    print("Third Test String: ", last_test_string)
    encoded_data, tree = huffman_encoding(last_test_string)
    print("The Huffman Code: ", encoded_data)
    decode = huffman_decoding(encoded_data, tree)
    print("The Decoded String ", decode)

    print("\n")

    last_test_string = ""
    print("Third Test String: ", last_test_string)
    encoded_data, tree = huffman_encoding(last_test_string)
    print("The Huffman Code: ", encoded_data)
    decode = huffman_decoding(encoded_data, tree)
    print("The Decoded String ", decode)