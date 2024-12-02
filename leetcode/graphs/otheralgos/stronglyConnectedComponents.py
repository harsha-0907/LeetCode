# To find the number of strongly connected components in a graph

from collections import deque

def stronglyConnectedComponents(n, edges):
    def reverseAdjacencyList(adj):
        adjT = [[] for _ in range(len(adj))]
        for i in range(len(adj)):
            for j in adj[i]:
                adjT[j].append(i)
        return adjT
        
    def dfs(node, parent):
        nonlocal dfs_list
        visited[node] = 1
        adjnodes = adj[node]
        for nextnode in adjnodes:
            if not visited[nextnode]:
                # If the node is not yet visited
                dfs(nextnode, node)
            
        dfs_list.appendleft(node)
        
    def lastTraversal(node, parent):
        visited[node] = 2
        adjnodes = adj[node]
        for nextnode in adjnodes:
            if visited[nextnode] != 2:
                lastTraversal(nextnode, node)
        
        
    visited = {i:0 for i in range(n)}
    dfs_list = deque()
    
    # We have obtained the dfs order of the graph
    for i in range(n):
        if visited[i] != 1:
            dfs(i, None)
        
    # Now reverse the complete graph to find the strongly connected components
    adj = reverseAdjacencyList(adj)
        
    count = 0
    # In the last traversal, we must start only from the node which can travel to all other node in the original graph
    # We cannot use the normal for loop as the node might be in the middle and when we reverse the graph, it can still 
    # go to other strongly connected graphs, to avoid it we must start from the left most which is obtained from the dfs_list
    # that is obtained in the first dfs.
    # That's why we use the nodes popped from the list instead of the for loop
    while dfs_list:
        node = dfs_list.popleft()
        if visited[node] != 2:
            lastTraversal(node, None)
            count += 1
    return count

adj = [[1, 2], [],[]]
print(reverseAdjacencyList(adj))