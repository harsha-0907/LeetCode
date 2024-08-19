# Create a tree from inorder and preorder traversal

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

def setNode(node, inorder, preorder):
    if not node:
        # Initialize the root node
        node = root= Node(preorder[0])
    left_num = getPosition(node.val, inorder)
    left_inorder = inorder[:left_num]
    left_preorder = preorder[1:left_num+1]

        # Right Nodes
    right_num = len(inorder) - (left_num + 1)
    right_inorder = inorder[left_num+1:]
    right_preorder = preorder[left_num+1:]

    if left_num > 0:
        left_node = Node(left_preorder[0])
        node.left = left_node
        setNode(left_node, left_inorder, left_preorder)
    else:
        node.left = None
        
    if right_num > 0:
        right_node = Node(right_preorder[0])
        node.right = right_node
        setNode(right_node, right_inorder, right_preorder)
    else:
        node.right = None
    return node
def preOrderTraversal(node):
    if not node:
        return None
    print(node.val)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

preorder = [3,9,20,15,7]; inorder = [9,3,15,20,7]
root = setNode(None, inorder, preorder)
preOrderTraversal(root)