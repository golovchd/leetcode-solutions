# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        max_level = -1
        max_sum = 0
        level = 0
        while queue:
            level += 1
            new_queue = []
            s = 0
            for node in queue:
                s += node.val
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            if max_level == -1 or s > max_sum:
                max_level = level
                max_sum = s
            queue = new_queue
        return max_level
