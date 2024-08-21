# Ceil in BST

def ceilBST(node, inp):
    max_num = -1

    while node:
        if node.key == inp:
            return node.key
        elif node.key > inp:
            max_num = node.key
            node = node.left
        else:
            node = node.right
    
    return max_num
