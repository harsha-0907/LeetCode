# To check if the given tree is a Binary Search Tree

ans = [True]
def checkBST(node, min_size, max_size):
    if not node:
        return None
    print(node.val, min_size, max_size, end = '')
    if node.val > min_size and node.val < max_size:
        print("True")
        # Going left
        checkBST(node.left, min_size, node.val)
        # Going Right
        checkBST(node.right, node.val, max_size)
    else:
        print("False")
        ans[0] = False
        return None

