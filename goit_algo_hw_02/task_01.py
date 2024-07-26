import random
from queue import Queue

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