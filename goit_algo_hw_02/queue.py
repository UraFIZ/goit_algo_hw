from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        return self.linked_list.is_empty()

    def enqueue(self, item):
        self.linked_list.append(item)

    def dequeue(self):
        return self.linked_list.delete_first()

    def front(self):
        if not self.is_empty():
            return self.linked_list.head.data
        return None

    def print_queue(self):
        self.linked_list.print_list()