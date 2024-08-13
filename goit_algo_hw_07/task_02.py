from typing import Optional, TypeVar

T = TypeVar('T')

class TreeNode:
    def __init__(self, value: T):
        self.value: T = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

def find_min(node: Optional[TreeNode]) -> Optional[T]:
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node.value