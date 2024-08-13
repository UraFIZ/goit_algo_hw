import time
import random
from tabulate import tabulate
from termcolor import colored

from greedy_algorithm import find_coins_greedy
from dynamic_programming import find_min_coins

def colorize(text, color):
    return colored(text, color)

def main():
    coins = [50, 25, 10, 5, 2, 1]
    # Generate 10 random test amounts from 10 to 100
    test_amounts = sorted(random.randint(10, 100) for _ in range(10))
    results = []

    for amount in test_amounts:
        start_greedy = time.perf_counter()
        result_greedy = find_coins_greedy(amount, coins)
        time_greedy = time.perf_counter() - start_greedy

        start_dp = time.perf_counter()
        result_dp = find_min_coins(amount, coins)
        time_dp = time.perf_counter() - start_dp

        # Colorize and format the results and times
        results.append([
            colorize(amount, 'yellow'),  # Amount column colored yellow
            colorize(str(result_greedy), 'magenta'),
            colorize(f"{time_greedy:.5f}", 'magenta'),
            colorize(str(result_dp), 'cyan'),
            colorize(f"{time_dp:.5f}", 'cyan')
        ])

    headers = [
        colorize("Amount", 'yellow'),  # Header for Amount colored yellow
        colorize("Greedy Result", 'magenta'), 
        colorize("Greedy Time (s)", 'magenta'),
        colorize("DP Result", 'cyan'), 
        colorize("DP Time (s)", 'cyan')
    ]
    
    # Using "grid" table format to ensure alignment and readability
    table = tabulate(results, headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
