# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Submition https://leetcode.com/submissions/detail/452839861/
    # Runtime: 108 ms, faster than 36.30% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
    # Memory Usage: 17.7 MB, less than 94.44% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
    # Time O(V), Memory O(V)
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [root]
        last = None
        gp_sum = 0
        while stack:
            cur = stack[-1]
            if not last or (last != cur.left and last != cur.right):
                # New node
                if len(stack) > 2 and stack[-3].val % 2 == 0:
                    gp_sum += cur.val
                if cur.left:
                    stack.append(cur.left)  # Going left
                elif cur.right:
                    stack.append(cur.right)  # Going right
                else:
                    last = stack.pop(-1)
            else:
                # returning to node
                if cur.right and cur.right != last:
                    stack.append(cur.right)  # Going right
                else:
                    last = stack.pop(-1)
        return gp_sum
