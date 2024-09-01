# To find the shortest path from starting point(i0, j0) to (i1, j1)
from collections import deque

def shortestPath(i_, j_,i1_, j1_, matrix):
    # This is for an 8-directional path in a matrix
    src = (i_, j_); dest = (i1_, j1_)
    queue = deque([(src, 0)]); empty = deque()
    m = len(matrix); n = len(matrix[0])
    distances = {src: 0}

    while queue != empty: 
        pos = queue.popleft()
        print(pos[0])
        (i, j) = pos[0]
        distance = pos[1] + 1
        for i_ in [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1)]:
            i1 = i + i_[0]; j1 = j + i_[1]
            if i1 >= 0 and i1 < m:
                if j1 >= 0 and j1 < n:
                    if matrix[i1][j1] == 0:
                        #print(i1, j1)
                        if (i1, j1) == dest:
                            return distance+1
                        else:    
                            if (i1, j1) in distances:
                                if distances[(i1, j1)] > distance:
                                    queue.append([(i1, j1), distance])
                                    distances[(i1, j1)] = distance
                            else:
                                distances[(i1, j1)] = distance
                                queue.append([(i1, j1), distance])
    
    return -1


matrix = [[0,0,0],[0,0,0],[0,0,0]]
src = (0, 0); dest = (len(matrix)-1, len(matrix)-1)
#print(dest)
res = shortestPath(0,0, dest[0], dest[1], matrix)

print(res)
