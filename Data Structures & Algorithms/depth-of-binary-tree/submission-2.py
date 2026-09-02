# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # off rip, I'm thinking since time complx is O(n) I can just 
        # count everything and evaluate log(n)
        return self.depthHelper(root, 0)

    def depthHelper(self, root, currDepth) -> int:
        if not root: return currDepth

        currDepth += 1
        right = self.depthHelper(root.right, currDepth)
        left = self.depthHelper(root.left, currDepth)
        return max(right, left)

