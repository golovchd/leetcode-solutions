# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        o_stack = [original]
        c_stack = [cloned]
        last = None
        while o_stack:
            o_cur = o_stack[-1]
            c_cur = c_stack[-1]
            # New node
            if not last or (last != o_cur.left and last != o_cur.right):
                # Check if we found target
                if o_cur == target:
                    return c_cur
                if o_cur.left:
                    o_stack.append(o_cur.left)
                    c_stack.append(c_cur.left)
                elif o_cur.right:
                    o_stack.append(o_cur.right)
                    c_stack.append(c_cur.right)
                else:
                    last = o_stack.pop(-1)
                    c_stack.pop(-1)
            else:
                # Return from left, have right
                if o_cur.right and o_cur.right != last:
                    o_stack.append(o_cur.right)
                    c_stack.append(c_cur.right)
                else:
                    last = o_stack.pop(-1)
                    c_stack.pop(-1)
