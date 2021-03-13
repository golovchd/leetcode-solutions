# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMovesAndExcessive(self, node: TreeNode) -> (int, int):
        if not node:
            return 0, 0
        left_excessive, left_moves = self.getMovesAndExcessive(node.left)
        right_excessive, right_moves = self.getMovesAndExcessive(node.right)
        excessive = node.val + left_excessive + right_excessive - 1
        moves = abs(left_excessive) + abs(right_excessive) + left_moves + right_moves
        return excessive,  moves
            
        
    def distributeCoins(self, root: TreeNode) -> int:
        _, moves = self.getMovesAndExcessive(root)
        return moves
