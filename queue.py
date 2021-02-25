class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, value):
        node = Node(value)

        if self._size == 0:
            self.last = node
            self.first = node
        else:
            self.last.next = node
            self.last = node

        self._size += 1

    def pop(self):
        if self._size > 0:
            self.first = self.first.next
            self._size -= 1

    def __repr__(self):
        r = ""
        pointer = self.first
        while(pointer):
            r = f'{r}{str(pointer.value)} | '
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


queue = Queue()

queue.push(200)
queue.push(300)
queue.push(500)
queue.push(600)
print(queue)

queue.pop()
print(queue)
