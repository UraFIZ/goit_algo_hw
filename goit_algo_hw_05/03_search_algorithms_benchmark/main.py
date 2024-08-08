import timeit
import os
from tabulate import tabulate
from termcolor import colored
from algorithms.boyer_moore import boyer_moore
from algorithms.kmp_search import kmp_search
from algorithms.rabin_karp import rabin_karp

def read_file(file_path):
    print(f"Looking for file at: {file_path}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def measure_time(algorithm, text, pattern):
    setup_code = f"from __main__ import {algorithm.__name__}"
    stmt = f"{algorithm.__name__}({repr(text)}, {repr(pattern)})"
    times = timeit.repeat(stmt, setup=setup_code, repeat=3, number=1)
    return min(times)

def main():
    base_dir = "data"
    files = ["01_article.txt", "02_article.txt"]
    patterns = {
        "existing": "алгоритм",
        "non_existing": "немаєтакогослова"
    }
    algorithms = [boyer_moore, kmp_search, rabin_karp]

    results = []

    for file_name in files:
        file_path = os.path.join(base_dir, file_name)
        text = read_file(file_path)
        if text is None:
            continue  # Пропускаємо файл, якщо його не знайдено
        for pattern_type, pattern in patterns.items():
            for algorithm in algorithms:
                time_taken = measure_time(algorithm, text, pattern)
                results.append({
                    "Algorithm": algorithm.__name__,
                    "Text": file_name,
                    "Pattern Type": pattern_type,
                    "Time (s)": time_taken
                })

    headers = ["Algorithm", "Text", "Pattern Type", "Time (s)"]
    rows = [
        [colored(result["Algorithm"], 'cyan'), 
         colored(result["Text"], 'yellow'), 
         colored(result["Pattern Type"], 'green'), 
         colored(f"{result['Time (s)']:.6f}", 'magenta')]
        for result in results
    ]
    print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))

if __name__ == "__main__":
    main()
