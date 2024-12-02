# Delete a node in BST

# Here we use DFS to find the node and its parent
parent = None; dirn = ''
def searchNode(node):
    if node.left:
        if node.left.val == target:
            parent = node; dirn = 'L'
            return (node, 'L')
        res = searchNode(node.left)
    if res:
        return res
    if node.right:
        if node.right.val == target:
            parent = node; dirn = 'R'
            return (node, 'R')
        return searchNode(node.right)

parent, dirn = searchNode(root)

def removeNode(parent, dirn):
    if dirn == 'L':
        node = parent.left
        if not node.left and not node.right:
            parent.left = None
    else:
        node = parent.right
        if not node.left and not node.right:
            parent.right = None
    
    # We will go to the first right and left-most node else first left and right-most node

    if node.right:
        child = parent = node.right
        while child:
            parent = child
            child = child.left
        if parent.right:
            node.right.left = parent.right
        node.val = parent.val
    
    else:
        child = parent = node.left
        while child:
            parent = child
            child = child.right
        if parent.left:
            node.left.right= parent.left
        
        node.val = parent.val





        