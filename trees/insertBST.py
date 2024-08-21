# Insert a Node in a BST

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertIntoBST(node, value):
    n1 = node
    if not node:
        return Node(value)
    
    while node:
        if node.val > value:
            if node.left:
                node = node.left
            else:
                node.left = Node(value)
                break
        else:
            if node.right:
                node = node.right
            else:
                node.right = Node(value)
                break
    return n1
    
    
    node.