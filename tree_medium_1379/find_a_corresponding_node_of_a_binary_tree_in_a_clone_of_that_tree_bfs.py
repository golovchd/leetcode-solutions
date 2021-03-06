# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        o_queue = [original]
        c_queue = [cloned]
        last = None
        while o_queue:
            new_o_queue = []
            new_c_queue = []
            for i in range(len(o_queue)):
                if o_queue[i] == target:
                    return c_queue[i]
                if o_queue[i].left:
                    new_o_queue.append(o_queue[i].left)
                    new_c_queue.append(c_queue[i].left)
                if o_queue[i].right:
                    new_o_queue.append(o_queue[i].right)
                    new_c_queue.append(c_queue[i].right)
            o_queue = new_o_queue
            c_queue = new_c_queue
