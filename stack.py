class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            self.top = self.top.next
            self._size -= 1

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = f'{r}{str(pointer.value)}\n'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


stack = Stack()

stack.push(200)
stack.push(300)
stack.push(500)
stack.push(600)
print(stack)

stack.pop()
print(stack)
