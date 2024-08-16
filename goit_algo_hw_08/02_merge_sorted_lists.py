import heapq
from typing import List, Tuple

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int, int]] = []
    
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    merged_list: List[int] = []
    
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)
        
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple: Tuple[int, int, int] = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

lists: List[List[int]] = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list: List[int] = merge_k_lists(lists)
print("Відсортований список:", merged_list)