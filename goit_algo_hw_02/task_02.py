from deque import Deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо в нижній регістр
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    deque = Deque()
    
    # Додаємо всі символи до двосторонньої черги
    for char in s:
        deque.add_rear(char)
    
    # Порівнюємо символи з обох кінців
    while not deque.is_empty() and deque.front() == deque.rear():
        if len(s) > 1:
            deque.remove_front()
            deque.remove_rear()
        else:
            deque.remove_front()
    
    # Якщо черга порожня, рядок є паліндромом
    return deque.is_empty()

def main():
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "Hello, World!",
        "Madam, I'm Adam",
        ""
    ]
    
    for s in test_strings:
        print(f"'{s}' is palindrome: {is_palindrome(s)}")

if __name__ == "__main__":
    main()