import heapq
from typing import List

def min_cost_to_connect_cables(cables: List[int]) -> int:
    heapq.heapify(cables)
    total_cost: int = 0

    while len(cables) > 1:
        first: int = heapq.heappop(cables)
        second: int = heapq.heappop(cables)
        cost: int = first + second
        total_cost += cost
        heapq.heappush(cables, cost)
    
    return total_cost

cables: List[int] = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))