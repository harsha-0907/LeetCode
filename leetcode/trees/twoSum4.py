# To find if the tree has 2 numbers that equal sum 'k'

queue = []
def preOrderTraversal(node):
    if not node:
        return None
    else:
        preOrderTraversal(node.left)
        queue.append(node.val)
        preOrderTraversal(node.right)

def findSum(queue, k):
    start = end = 0
    for end in range(1, len(queue)):
        if queue[start] + queue[end] > k:
            break
        elif queue[start] + queue[start] == k:
            return True
    
    # end - is the max position of the biggest element that fits the description
    while start < end:
        if queue[start] + queue[end] == k:
            return True
        elif queue[start] + queue[end] < k:
            start += 1
        else:
            end -= 1
    
    return False
