# To find the least common acestor
def leastCA(p, q, root):
    if p.val < q.val:
        p, q = q, p
            
            # p > q
    print(p.val, q.val)

    while root:
        if root.val < q.val:
            root = root.right
        elif root.val > p.val:
            root = root.left
        elif root.val <= p.val or root.val >= q.val:
            return root
            
    return root

