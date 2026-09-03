# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first write out with a helper, then condense

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # iterate through the entire tree
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    q.append(node.right)
                    q.append(node.left)

                    right = self.heightHelper(node.right)
                    left = self.heightHelper(node.left)

                    if abs(right - left) > 1:
                        return False
                
        return True


    def heightHelper(self, root, level=0):
        if not root:
            return level
        
        left = self.heightHelper(root.left, level)
        right = self.heightHelper(root.right)
        
        return 1 + max(left, right)