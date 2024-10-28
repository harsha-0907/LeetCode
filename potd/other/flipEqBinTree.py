class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False
        checkIfTreeValueSame = self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
        checkIfTreeValueNeedsFlip = (self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))
        return checkIfTreeValueSame or checkIfTreeValueNeedsFlip