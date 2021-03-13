"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur = root
        last = root
        while cur:
            if cur.left:
                last.next = cur.left
                last = last.next
            if cur.right:
                last.next = cur.right
                last = last.next
            last.next = None
            cur = cur.next
        cur = root
        while cur:
            cur.next = None
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        return root
