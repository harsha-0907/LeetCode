# To find the max number of moves that can be made in a grid
# We will be using DP

def maxMoves(grid):
    # We will move only(NE, E, SE) -> moving east is mandatory
    # The next element must be strictly greater than the previous element
    def moveNext(ele, pos):
        print(ele, pos)
        x, y = pos
        # x, y = col, row
        if (x, y) in memory:
            return memory[(x, y)]
        else:
            if y >= col-1:
                # No next element
                return 1
            dist = 0
            # Moving NE
            if x > 0 and grid[x-1][y+1] > ele:
                dist = max(dist, moveNext(grid[x-1][y+1], (x-1, y+1)))
            # Moving SE
            if x+1 < row and grid[x+1][y+1] > ele:
                dist = max(dist, moveNext(grid[x+1][y+1], (x+1, y+1)))
            if grid[x][y+1] > ele:
                dist = max(dist, moveNext(grid[x][y+1], (x, y+1)))
            
            memory[(x, y)] = dist+1
            return memory[(x, y)]
        
    row, col = len(grid), len(grid[0]); maxdist = 0
    memory = dict()
    for pos in range(row):
        maxdist = max(moveNext(grid[pos][0], [pos,0]), maxdist) # npos -> (x, y)
        print(maxdist)
    return maxdist-1

grid = [[3,2,4],[2,1,9],[1,1,7]]

res = maxMoves(grid)

print(res)