# To find all the possible number of graphs

def countPossibleGraphs(n):
    total_edges = (n *(n-1)) // 2
    return 2 ** total_edges

print(countPossibleGraphs(5))