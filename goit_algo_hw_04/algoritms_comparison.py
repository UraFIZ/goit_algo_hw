import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr):
    return sorted(arr)

def generate_data(size, data_type='random'):
    if data_type == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(1, size + 1))
    elif data_type == 'reverse':
        return list(range(size, 0, -1))
    else:
        raise ValueError("Invalid data type")

def measure_time(sort_func, arr):
    return timeit.timeit(lambda: sort_func(arr.copy()), number=1)

def compare_algorithms(sizes, data_type='random'):
    print(f"\nПорівняння алгоритмів сортування ({data_type} дані):")
    print(f"{'Розмір':>10} | {'Insertion Sort':>15} | {'Merge Sort':>15} | {'Timsort':>15}")
    print("-" * 62)

    for size in sizes:
        data = generate_data(size, data_type)
        
        insertion_time = measure_time(insertion_sort, data)
        merge_time = measure_time(merge_sort, data)
        timsort_time = measure_time(timsort, data)

        print(f"{size:10d} | {insertion_time:15.6f} | {merge_time:15.6f} | {timsort_time:15.6f}")

# Тестування алгоритмів
sizes = [100, 500, 1000, 5000, 10000]
compare_algorithms(sizes, 'random')
compare_algorithms(sizes, 'sorted')
compare_algorithms(sizes, 'reverse')