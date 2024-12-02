# Serialize and De-Serialize the tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(node):
    queue.append(node); maxl = 1; cnt = 0
    #storage = []
    while cnt < maxl:
        node = queue[cnt]
        if not node:

            pass
        else:
            queue.append(node.left)
            queue.append(node.right)
            queue[cnt] = node.val
            maxl = len(queue)
        cnt += 1
    return queue


def deserialize():
    if queue == []:
        return None
    front = 0; back = 1; length = len(queue)
    root = Node(queue[front])
    queue[front] = root

    while back < length:
        if queue[front] == None:
            front += 1
            continue
        node = queue[front]
        if queue[back] == None:
            node.left = None
        else:
            n = Node(queue[back])
            queue[back] = n
            node.left = n
        back += 1
        
        # Now for the right subtree
        if queue[back] == None:
            node.right = None
        else:
            n = Node(queue[back])
            #print(queue[back])
            queue[back] = n
            node.right = n
        back += 1
        front += 1
    
    return root

def levelTraversal(root):
    queue = [root]
    while queue != []:
        node = queue[0]
        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            print(None)
        queue.pop(0)

def preOrder(node)    :
    if not node:
        print(None)
    else:
        print(node.val)
        preOrder(node.left)
        preOrder(node.right)

queue = [4, 2, 3, None, None, None, None]
root = deserialize()
levelTraversal(root)
preOrder(root)
    