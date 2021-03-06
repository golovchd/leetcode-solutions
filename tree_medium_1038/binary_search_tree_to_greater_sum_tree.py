# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        stack = [root]
        last = None
        total = 0
        while stack:
            cur = stack[-1]
            if not last or (last != cur.left and last != cur.right):
                # New node, going right first
                if cur.right:
                    stack.append(cur.right)
                elif cur.left:
                    # Had no right, use total from parent only
                    total += cur.val
                    cur.val = total
                    stack.append(cur.left)
                else:
                    # Leaf
                    total += cur.val
                    cur.val = total
                    # returning
                    last = stack.pop(-1)
            else:
                if cur.right and last == cur.right:
                    # Returned from right or have no right, adding
                    total += cur.val
                    cur.val = total
                if cur.left and cur.left != last:
                    stack.append(cur.left)
                else:
                    last = stack.pop(-1)
        return root
    