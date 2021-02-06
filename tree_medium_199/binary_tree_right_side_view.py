# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Submition https://leetcode.com/submissions/detail/452865696/
    # Runtime: 28 ms, faster than 90.22% of Python3 online submissions for Binary Tree Right Side View.
    # Memory Usage: 14.4 MB, less than 21.65% of Python3 online submissions for Binary Tree Right Side View.
    # Time O(V), Memory O(V)
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Depth First Search
        if not root:
            return []
        rsv = []
        queue = [root]
        while queue:
            rsv.append(queue[-1].val)
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rsv
