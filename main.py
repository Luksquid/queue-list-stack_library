from typing import Any

class Node:
    value: Any
    next: 'Node'


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def len(self) -> Node:
        temp = self.head
        wyn = 0
        if (self.head == None):
            return 0
        while (True):
            wyn = wyn + 1
            if (temp.next == None):
                break
            temp = temp.next
        return wyn;

    def push(self, value: Any) -> None:

        temp = Node()
        f = False
        if (self.head == None):
            f = True
        temp.value = value
        temp.next = self.head
        self.head = temp
        if (f == True):
            self.tail = self.head
            f = False

    def append(self, value: Any) -> None:

        temp = Node()
        temp.value = value
        temp.next = None
        if (self.tail != None):
            self.tail.next = temp
        self.tail = temp
        if (self.head == None):
            self.head = self.tail

    def show(self) -> Node:
        temp = self.head
        while (True):
            print(temp.value)
            if (temp.next == None):
                break
            temp = temp.next

    def node(self, at: int) -> Node:

        temp = self.head
        for i in range(0, at):
            temp = temp.next
        return temp

    def insert(self, value: Any, after: Node) -> None:

        temp = Node()
        temp.value = value
        temp.next = after.next
        after.next = temp

    def pop(self) -> Any:

        temp = self.head
        self.head = self.head.next
        return temp

    def remove_last(self) -> Any:

        temp = self.head
        while (temp.next.next != None):
            temp = temp.next
        t = temp.next
        temp.next = None
        self.tail = temp
        return t

    def remove(self, after: Node) -> Any:

        temp = after.next.next
        after.next = after.next.next
        return temp

    def print(self):
        print(str(self.head.value) + " -> " + str(self.head.next.value))

    def __str__(self):

        temp = self.head
        t = ""
        while (True):
            t = t + str(temp.value)
            if (temp.next == None):
                break
            temp = temp.next
            t = t + " -> "
        return t

class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return self._storage.len()

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def print(self):
        self._storage.show()

    def pop(self):
        return self._storage.pop()


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return self._storage.len()

    def __str__(self):
        temp = self._storage.head
        t = ""
        while (True):
            t = t + str(temp.value)
            if (temp.next == None):
                break
            temp = temp.next
            t = t + ", "
        return t

    def peak(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def print(self):
        self._storage.show()

list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element.value

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element.value
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

# //////////////////////////////////////////////


stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value.value == 1

assert len(stack) == 2

# //////////////////////////////////////////////

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first.value == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2