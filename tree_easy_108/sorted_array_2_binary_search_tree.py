# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Submition https://leetcode.com/submissions/detail/452834692/
    # Runtime: 72 ms, faster than 70.74% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    # Memory Usage: 16.5 MB, less than 69.87% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    # Time O(n), Memory O(n)
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if not n:
            return None
        return self.getTree(nums, 0, n - 1)

    def getTree(self, nums: List[int], s: int, e: int) -> TreeNode:
        median = (s + e) // 2
        root = TreeNode(nums[median])
        if median > s:
            root.left = self.getTree(nums, s, median - 1)
        if median < e:
            root.right = self.getTree(nums, median + 1, e)
        return root
