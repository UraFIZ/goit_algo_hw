from linked_list import LinkedList

class Deque:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        return self.linked_list.is_empty()

    def add_front(self, item):
        self.linked_list.prepend(item)

    def add_rear(self, item):
        self.linked_list.append(item)

    def remove_front(self):
        return self.linked_list.delete_first()

    def remove_rear(self):
        return self.linked_list.delete_last()

    def front(self):
        if not self.is_empty():
            return self.linked_list.head.data
        return None

    def rear(self):
        if not self.is_empty():
            return self.linked_list.tail.data
        return None