from typing import Optional, TypeVar

T = TypeVar('T')

class TreeNode:
    def __init__(self, value: T):
        self.value: T = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

def sum_tree_values(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    return node.value + sum_tree_values(node.left) + sum_tree_values(node.right)