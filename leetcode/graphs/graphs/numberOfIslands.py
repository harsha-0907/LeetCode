# To obtain the number of islands in a matrix

# Let us consider that the dimensions of the matrix will be less than 25*25.

import random
import time

def generate_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        matrix.append(row)
    return matrix

# Extra Time-Complexity
def numberOfIslands(matrix):
    def bfs(cnt):
        while len(visited) > cnt:
            pos = visited[cnt]; cnt += 1
            (i, j) = pos
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            for dirn in directions:
                if not (i+dirn[0] < 0 or i+dirn[0] >= m or j+dirn[1] < 0 or j+dirn[1] >= n) and (i+dirn[0], j+dirn[1]) not in visited and matrix[i+dirn[0]][j+dirn[1]] == 1:
                    visited.append((i+dirn[0], j+dirn[1]))
        return cnt

    m = len(matrix); n = len(matrix[0])
    visited = []; cnt = 0; islands = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and matrix[i][j] == 1:
                # If the position is not yet visited
                #print((i, j))
                visited.append((i, j))
                cnt = bfs(cnt)
                islands += 1
    #print(visited)
    return islands

# Extra Space-Complexity
def numberOfIslands2(matrix):
    def bfs1(i, j):
        visited = [(i, j)]; cnt1 = 0
        while len(visited) > cnt1:
            node = visited[cnt1]; cnt1 += 1
            (i, j) = node
            matrix1[i][j] = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            for dirn in directions:
                if not (i+dirn[0] < 0 or i+dirn[0] >= m or j+dirn[1] < 0 or j+dirn[1] >= n) and matrix1[i+dirn[0]][j+dirn[1]] == 1 and (i+dirn[0], j+dirn[1]) not in visited:
                    visited.append((i+dirn[0], j+dirn[1]))
        return None

    m = len(matrix); n = len(matrix[0])
    cnt = 0
    matrix1 = [[element for element in row] for row in matrix]
    for i in range(m):
        for j in range(n):
            if matrix1[i][j] == 1:
                bfs1(i, j)
                cnt += 1
    return cnt

#matrix = [[0, 1, 1, 0, 1, 0, 0],[0, 0, 1, 1, 0, 1, 0]]
matrix = generate_matrix(100, 100)
t1 = time.time()
res = numberOfIslands(matrix)
print(res)
t2 = time.time()
res1 = numberOfIslands2(matrix)
t3 = time.time()
print(res1)
print(t2-t1, t3-t2)
                