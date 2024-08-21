# Create a BST from the preorder traversal

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if not node:
        return None
    inOrderTraversal(node.left)
    print(node.val)
    inOrderTraversal(node.right)

def dividePreOrder(value, beg, end):
    for i in range(beg, end):
        if preorder[i] > value:
            return i
    # If no number exists greater than value
    return end

root = None
def createBST(node, begin, end):
    if not node:
        # Initialize the root node
        root = node = TreeNode(preorder[begin])

    pos = dividePreOrder(node.val, begin+1, end)
    left_num = pos - begin  -1  # Number of left nodes
    right_num = end - pos   # NUmber of right nodes
    if left_num != 0:
        left_node = TreeNode(preorder[begin+1])
        node.left = left_node
        createBST(left_node, begin+1, pos)
    if right_num != 0:
        right_node = TreeNode(preorder[pos])
        node.right = right_node
        createBST(right_node, pos, end)
    return node

preorder = [8,5,1,7,10,12]
length = len(preorder)
n1 = createBST(None, 0, length)
inOrderTraversal(n1)