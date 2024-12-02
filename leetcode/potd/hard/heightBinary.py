# To find the height of the tree after performing the queries
# Approaches:
            # 1. For each query, run the max depth after removing the element (Brute)
            # 2. For every node, calculate its height and remove the height from the max height
            # 3. Calculate all the nodes that are present in tree and calculate the height

# This  is a optimized-brute force approach
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def calculatePosition(node, path):
            if node:
                positions[node.val-1] = path
                left = calculatePosition(node.left, path+'0')
                right = calculatePosition(node.right, path+'1')
                positions[node.val-1] = (left, right, path)
                return max(left, right) + 1
            else:
                return 0
        
        positions = [[]]*(10**5)
        max_height = calculatePosition(root, '')
        if max_height == positions[root.val-1][0] and max_height == positions[root.val-1][1]:
            return [max_height]*len(queries)
        
        # Now we can process the queries
        def solveQuery(node, path):
            h = 0; dirn = path[0]
            height, other_height = positions[node.val-1][int(dirn)], positions[node.val-1][int(not int(dirn))]
            node = node.left if dirn == '0' else node.right
            for dirn in path[1:-1]:
                h += 1
                height, other_height = positions[node.val-1][int(dirn)], max(other_height, positions[node.val-1][int(not int(dirn))]+h)
                node = node.left if dirn == '0' else node.right
            
            return other_height
                
        return [solveQuery(root, positions[target-1][2]) for target in queries]
                    

# This is the optimized approach
class Solution:
    def __init__(self):
        self.mp1 = {}
        self.mp2 = {}
        self.sz = {}
        self.id = 0
    
    def treeQueries(self, root: Optional[TreeNode], q: List[int]) -> List[int]:
        self.dfs(root, 0)
        left = [0] * self.id
        right = [0] * self.id
        
        for i in range(self.id):
            left[i] = self.mp2[i]
            if i > 0:
                left[i] = max(left[i - 1], left[i])
        
        for i in range(self.id - 1, -1, -1):
            right[i] = self.mp2[i]
            if i + 1 < self.id:
                right[i] = max(right[i], right[i + 1])
        
        ans = []
        for node in q:
            nodeid = self.mp1[node]
            l, r = nodeid, nodeid + self.sz[nodeid] - 1
            h = 0
            if l > 0:
                h = max(h, left[l - 1])
            if r + 1 < self.id:
                h = max(h, right[r + 1])
            ans.append(h)
        
        return ans
    
    def dfs(self, root: Optional[TreeNode], h: int) -> int:
        if not root:
            return 0
        self.mp1[root.val] = self.id
        self.mp2[self.id] = h
        self.id += 1
        lz = self.dfs(root.left, h + 1)
        rz = self.dfs(root.right, h + 1)
        self.sz[self.mp1[root.val]] = 1 + lz + rz
        return 1 + lz + rz

