#a node which is composed of a binary search tree
#key will be a client's account ex) XXXX
#value will be a account object
class node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def set_value(self, value):
        self.value = value

    def set_key(self, key):
        self.key = key

    def set_left(self, node):
        self.left_child = node

    def set_right(self, node):
        self.right_child = node

    def is_leaf(self):
        return self.left_child == None and self.right_child == None

    def __str__(self):
        return str(self.key) + " " + str(self.value)

#binary search tree that stores the account objects
class bst:
    def __init__(self):
        self._count = 0
        self._root = None

    def get(self, key):
        current_node = self._root
        while current_node != None:
            if current_node.key == key:
                return current_node.value
            elif current_node.key > key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None

    def __getitem__(self, key):
        return self.get(key)
    #insert a account number as a key and an account object as a value in a node and store the node in the bst
    def put(self, key, value):
        if self.is_empty():
            self._root = node(key, value)
            self._count = 1
            return
        current_node = self._root
        while True:
            if current_node.key == key:
                current_node.value = value
                return
            elif current_node.key > key:
                if current_node.left_child == None:
                    new_node = node(key, value)
                    current_node.left_child = new_node
                    break
                else:
                    current_node = current_node.left_child
            else:
                if current_node.right_child == None:
                    new_node = node(key, value)
                    current_node.right_child = new_node
                    break
                else:
                    current_node = current_node.right_child
        self._count += 1

    def __setitem__(self, key, data):
        self.put(key, data)

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def in_order_traversal(self, func):
        self.in_order_traversal_rec(self._root, func)

    def in_order_traversal_rec(self, node, func):
        if node != None:
            self.in_order_traversal_rec(node.left_child, func)
            func(node.key, node.value)
            self.in_order_traversal_rec(node.right_child, func)

    def print_tree(self):
        self.in_order_traversal(self.print_node)

    def print_node(self, key, value):
        print(key, value)

    def remove(self, key):
        # First Handle Empty Tree
        if self._root == None:
            return False
        # Handle removal of root
        if self._root.key == key:
            self._count -= 1
            if self._root.left_child == None:
                self._root = self._root.right_child
            elif self._root.right_child == None:
                self._root = self._root.left_child
            else:
                replace_node = self.get_remove_right_small(self._root)
                self._root.key = replace_node.key
                self._root.value = replace_node.value
        # Find node which holds key by having current node stop at parent of found node
        else:
            current_node = self._root
            while current_node != None:
                # Following code deal with the case where left child has key
                if current_node.left_child and current_node.left_child == key:
                    found_node = current_node.left_child
                    if found_node.is_leaf():
                        current_node.left_child = None
                    elif found_node.right_child == None:
                        current_node.left_child = found_node.left_child
                    elif found_node.left_child == None:
                        current_node.left_child = found_node.right_child
                    else:
                        replace_node = self.get_remove_right_small(found_node)
                        found_node.key = replace_node.key
                        found_node.value = replace_node.value
                        self._count -= 1
                        return True
                # Following code deals with the case where right child has key
                elif current_node.right_child and current_node.right_child.key == key:
                    found_node = current_node.right_child
                    if found_node.is_leaf():
                        current_node.right_child = None
                    elif found_node.left_child == None:
                        current_node.right_child = found_node.right_child
                    elif found_node.right_child == None:
                        current_node.right_child = found_node.left_child
                    else:
                        replace_node = self.get_remove_right_small(found_node)
                        found_node.key = replace_node.key
                        found_node.value = replace_node.value
                        self._count -= 1
                        return True

    def get_remove_right_small(self, anode):
        current_node = anode.get_right()
        while current_node.get_left() != None:
            current_node = current_node.get_left()
        new_node = anode.node(current_node.get_key(), current_node.get_value())
        current_node.set_key(None)
        current_node.set_value(None)
        return new_node