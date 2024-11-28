# Maximum Path Sum 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(root):
        def calculatePath(node, height, maxheight):
            if not node:
                return 0
            else:
                left = calculatePath(node.left, height, maxheight)
                right = calculatePath(node.right, height, maxheight)

                if left + right + node.val > maxheight:
                    maxheight = left + right + node.val
                return maxheight, max(left, right) + node.val
        res = calculatePath(root, 0, 0)
        print(res)
        return res[0]

