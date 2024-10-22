# To find the kth largest sum(same level) in the tree.
Link : "https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description"
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left, right):
        self.val = val
        self.right = right
        self.left = left


def findKthLargest(root: Optional[TreeNode], k: int):
    def findNodes(node, height):
        if node:
            array.append((node.val, height))
            findNodes(node.left, height+1)
            findNodes(node.right, height+1)
    
    if not root:
        return -1
    else:
        array = []
        findNodes(root, 0)
        dict1 = dict(); maxell = 0
        for ele, height in array:
            if height in dict1:
                dict1[height] += ele
            else:
                dict1[height] = ele
        if len(dict1) < k:
            return -1
        else:
            return sorted(dict1.values, reverse=True)[k-1]
                