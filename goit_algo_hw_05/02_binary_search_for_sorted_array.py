def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            upper_bound = arr[mid]

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
    
    return (iterations, upper_bound)

# Приклад використання:
sorted_array = [0.1, 0.5, 1.2, 3.3, 4.4, 5.8, 7.7, 9.6]
target_value = 5.0

result = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}")
print(f"Верхня межа: {result[1]}")
