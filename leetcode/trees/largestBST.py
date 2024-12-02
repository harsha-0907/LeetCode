# To find the larget BST in a Binary Tree
"""
Here, we need to build the BST from the lower or leaf nodes
"""

def largestBST(node):
    if not node.left and not node.right:
        return (1, node.data, node.data)
            
    if node.left:
        lcnt, llow, lhigh = largestBST(node.left)
    else:
        lcnt, llow, lhigh = (0, node.data, None)
            
    if node.right:
        rcnt, rlow, rhigh = largestBST(node.right)
    else:
        rcnt, rlow, rhigh = (0, None, node.data)
            
    if (lhigh == None or lhigh < node.data) and (rlow == None or rlow > node.data):    
        return (lcnt + rcnt + 1, llow, rhigh)
    else:
        return (max(lcnt, rcnt), -float("inf"), float("inf"))
            



