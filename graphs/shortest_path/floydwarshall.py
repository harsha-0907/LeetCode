# Floyd-Warshall Algorithm to find the shortest path between different nodes

def floydWarshall(edges):
    # To find the shortest path from each node to another in the graph
    # Prepare the matrix for further operations
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                # Edge doesn't exist
                matrix[i][j] = float('inf')
    #print(matrix)
    
    for mid in range(n):
        # For each middle element
        for i in range(n):
            for j in range(n):
                if i == mid or j == mid or i == j:
                    continue
                matrix[i][j] = min(matrix[i][j], (matrix[i][mid] + matrix[mid][j]))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = -1
    return matrix
    
matrix = [[0, 1, 43],[1, 0, 6],[-1, -1, 0]]
res = floydWarshall(matrix)

print(res)