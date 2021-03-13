# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirStat(self, node : TreeNode, path_min: int, path_max: int):
        path_min = min(path_min, node.val)
        path_max = max(path_max, node.val)
        diff = path_max - path_min
        if node.left:
            left_diff = self.getDirStat(node.left, path_min, path_max)
        else:
            left_diff = 0
        if node.right:
            right_diff = self.getDirStat(node.right, path_min, path_max)
        else:
            right_diff = 0
        return max(diff, left_diff, right_diff)
        
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.getDirStat(root, root.val, root.val)
