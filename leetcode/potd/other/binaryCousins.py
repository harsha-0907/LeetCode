# To  and replace the nodes with buinary tree cousins
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryCousins(root: Optional[TreeNode]):
    def findNodes(node: Optional[TreeNode], parent: Optional[TreeNode] = None, height: int=None):
        if height not in array:
            array[height] = dict()
            array[height]['total'] = 0
            
        if parent not in array[height]:
            array[height][parent] = []
            array[height][parent].append(0)
            
        array[height][parent].insert(0, (node.val, node))
        array[height][parent][-1] += node.val
        array[height]['total'] += node.val
                
        if node.left:
            findNodes(node.left, node, height+1)
        if node.right:
            findNodes(node.right, node, height+1)
    
    array = dict()
    findNodes(root, None, 0)
    for height in array:
        total = array[height]['total']
        for parent in array[height]:
            if parent != 'total':
                #print(array[height][parent])
                ptotal = array[height][parent][-1]
                for node in array[height][parent][:-1]:
                    node[1].val = total - ptotal
        
    return root
        
        
    
