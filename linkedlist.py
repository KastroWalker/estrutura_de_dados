class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._inverted = False

    def append(self, value):
        self.head = self.insert(self.head, value)

    def insert(self, node, value):
        if node == None:
            return Node(value)
        else:
            if self._inverted:
                if node.value < value:
                    newNode = Node(value)
                    newNode.next = node
                    return newNode
                else:
                    node.next = self.insert(node.next, value)
            else:
                if node.value > value:
                    newNode = Node(value)
                    newNode.next = node
                    return newNode
                else:
                    node.next = self.insert(node.next, value)
        return node

    def remove(self, value):
        self.head = self.delete(self.head, value)

    def delete(self, node, value):
        if node == None:
            return None
        else:
            if node.value == value:
                return node.next
            else:
                node.next = self.delete(node.next, value)

        return node

    def reverse(self):
        previous_node = None
        next_node = None
        current_node = self.head

        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node
        self._inverted = not self._inverted

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = f'{r}|{str(pointer.value)} '
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


linked_list = LinkedList()

# Adding values in the list
linked_list.append(100)
linked_list.append(200)
linked_list.append(300)
linked_list.append(300)  # Adding a duplicate value in the list
linked_list.append(400)

print(linked_list)

# Removing a value from the list
linked_list.remove(200)

print(linked_list)

# Removing an undefined value from the list
linked_list.remove(350)

# Inverting list values
linked_list.reverse()

print(linked_list)

# Adding values in the list
linked_list.append(150)

print(linked_list)
