# Here the problem statement requires to find the number of citites that are less than a threshold value

def findTheCity(n, edges, threshold):
    matrix = [[float('inf') for i in range(n)] for i in range(n)]
    
    for i in range(n):
        matrix[i][i] = 0
    
    for edge in edges:
        u_, v_, wt = edge
        matrix[u_][v_] = wt
        matrix[v_][u_] = wt
    # The matrix is ready
    for mid in range(n):
        for i in range(n):
            for j in range(n):
                if i == mid or j == mid or i == j:
                    continue
                matrix[i][j] = min(matrix[i][j], matrix[i][mid] + matrix[mid][j])
    

    # Complete the matrix
    #print(threshold)
    print(matrix)
    min_cities = float("inf")
    result_city = -1
    for i in range(n):
        cnt = 0
        for j in range(n):
            if matrix[i][j] <= threshold:
                cnt += 1
        if cnt <= min_cities:
            min_cities = cnt
            result_city = i
    
    return result_city


n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
threshold = 2

res = findTheCity(n, edges, threshold)

print(res)