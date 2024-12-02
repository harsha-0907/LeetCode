# Create a tree using In-oprder and Post-order traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getPosition(value, list1):
    for i in range(len(list1)):
        if list1[i] == value:
            return i
    
    # Worst case
    return -1

def setNode(node, inorder, postorder):
    if not node:
        node = root = Node(postorder[-1])
    
    left_num = getPosition(node.val, inorder)
    left_inorder = inorder[:left_num]
    left_postorder = postorder[:left_num]

    right_num = len(inorder) - (left_num + 1)
    right_inorder = inorder[left_num+1:]
    right_postorder = postorder[left_num:-1]

    if left_num > 0:
        left_node = Node(left_postorder[-1])
        node.left = left_node
        setNode(left_node, left_inorder, left_postorder)
    else:
        node.left = None
    
    if right_num > 0:
        right_node = Node(right_postorder[-1])
        node.right = right_node
        setNode(right_node, right_inorder, right_postorder)
    else:
        node.right = None
    
    return node


# Let us reduce the time-complexity by sending the positions instead of the array

def preOrderTraversal(node):
    if not node:
        return None
    print(node.val)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

inorder = [9,3,15,20,7]; postorder = [9,15,7,20,3]
root = setNode(None, inorder, postorder)
preOrderTraversal(root)



