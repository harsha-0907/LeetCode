# To find the path with minimum effort

from collections import deque
import heapq

def pathWithMinEffort(src, dest, matrix):
    queue = [(src, 0, {src})]
    min_height = float("inf")
    m = len(matrix); n = len(matrix[0])
    while queue:
        node = heapq.heappop(queue)
        #print(node)
        if node[0] == dest:
            #print(node[1])
            return node[1]
        else:
            i, j = node[0]; h = node[1]; path = node[2]
            for di in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                i1 = i + di[0]; j1 = j + di[1]
                if i1 < m and i1 >= 0 and j1 < n and j1 >= 0:
                    n1 = (i1, j1)
                    if n1 not in path:
                        dis = max(abs(matrix[i1][j1] - matrix[i][j]), h)
                        heapq.heappush(queue, ( n1, dis, path | {n1}))
            
    return -1


src = (0, 0)
matrix = [[1,2,3],[3,8,4],[5,3,5]]
dest = (len(matrix)-1, len(matrix[0])-1)

res = pathWithMinEffort(src, dest, matrix)

print(res)