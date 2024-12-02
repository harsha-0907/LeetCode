# Floor of a value in a BST

def floor(self, node, inp):
    max_num = -1

    while node:
        if node.data == inp:
            return node.data
        elif node.data > inp:
            node = node.left
        else:
            max_num = node.data
            node = node.right
    return max_num