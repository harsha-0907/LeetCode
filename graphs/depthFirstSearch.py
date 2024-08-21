# Depth First Search in a adjacency representation of graph

def dfsOfGraph(V, adj):
        # code here
        # print(adj)
        vis = [-1 for i in range(V+1)]
        ans = []
        dfs(V,adj,vis,ans,0)
        return ans
        
def dfs(V,adj,vis,ans,curr):
    ans.append(curr)
    vis[curr] = 1
    for i in adj[curr]:
        if(vis[i] == -1):
            dfs(V,adj,vis,ans,i)



v = 5
adj = [[2,3,1] , [0], [0,4], [0], [2]]
res = dfsOfGraph(v, adj)
print(res)

        