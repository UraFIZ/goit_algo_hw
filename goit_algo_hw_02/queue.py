#  я подивився курс по Linked List  свого улюбленого викладача з каналу Codevolution на JS. Він перевикористовував LinkedList для реалізації черги. Я вирішив зробити те ж саме на Python.
import random

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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

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

def generate_request():
    return f"Заявка #{random.randint(1000, 9999)}"

def process_request(queue):
    if not queue.is_empty():
        request = queue.dequeue()
        print(f"Обробка: {request}")
    else:
        print("Черга пуста")

def main():
    queue = Queue()
    while True:
        action = input("Виберіть дію (1 - створити заявку, 2 - обробити заявку, 3 - вийти, 4 - показати чергу): ")
        if action == '1':
            request = generate_request()
            queue.enqueue(request)
            print(f"Створено: {request}")
        elif action == '2':
            process_request(queue)
        elif action == '3':
            break
        elif action == '4':
            print("Поточна черга:")
            queue.print_queue()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()