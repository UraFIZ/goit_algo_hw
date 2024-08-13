from typing import Optional, TypeVar

T = TypeVar('T')

class TreeNode:
    def __init__(self, value: T):
        self.value: T = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

def find_max(node: Optional[TreeNode]) -> Optional[T]:
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node.value