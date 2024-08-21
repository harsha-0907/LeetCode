# To recover a BST from the Binary Tree(faukty BST)

queue = []
def inOrderTraversal(node):
    if not node:
        return None
    inOrderTraversal(node.left)
    queue.append(node.val)
    inOrderTraversal(node.right)

def checkError(list1):
    list12 = sorted(list1)
    for i in range(list1):
        if list1[i] != list12[i]:
            return (list1[i], list12[i])
    
    # It is an impossible case
    return (-1, -1)

def modifyTree(node):
    if not node:
        return None
    if node.val in targets:
        node.val = suml - node.val
    modifyTree(node.left)
    modifyTree(node.right)

inOrderTraversal(root)
targets = checkError(queue)
suml = sum(targets)
modifyTree(root)
return root    