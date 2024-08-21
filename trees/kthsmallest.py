# Kth smallest element

ans = 0
def kthSmallest(node, cnt):
    if not node:
        return cnt
    
    cnt = kthSmallest(node.left, cnt) + 1
    if cnt == k:
        ans = node.val
        return cnt
    return kthSmallest(node.right, cnt)

kthSmallest(root, 0)