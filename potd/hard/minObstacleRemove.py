# The minimum obstacles to remove to reach the corner

def minObstacle(matrix):
    def calculateShortestDistance(matrix):
        length, breadth = len(matrix[0]), len(matrix)
        # distances = [[float('inf')for i in range(length)] for j in range(breadth)]
        queue = deque[(0, 0, 0)] # (obstacle_removed, x, y)
        visited = [[False] for i in range(length) for k in range(breadth)]
        visited[0][0] = True
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]        
        
        while queue:
            x, y, obstacle_removed = queue.pop_left()

            if x == length-1 and y == breadth-1:
                return obstacle_removed
            
            for dx, dy in directions:
                nx, ny = x+dx, y+dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        queue.appendleft((nx, ny, obstacle_removed))
                    else:
                        queue.appendleft((nx,ny, obstacle_removed+1))
        
        return -1
        

