#  я подивився курс по Linked List  свого улюбленого викладача з каналу Codevolution на JS. Він перевикористовував LinkedList для реалізації черги. Я вирішив зробити те ж саме на Python.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_first(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def delete_last(self):
        if self.is_empty():
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data
        current = self.head
        while current.next != self.tail:
            current = current.next
        data = self.tail.data
        self.tail = current
        self.tail.next = None
        return data

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")