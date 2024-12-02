# The Minimum Falling Path Sum using DP

def minimumFailingPathSum(grid):
    m = len(grid); n = len(grid[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    # Initialize the first array of dp
    for i in range(n):
        dp[0][i] = grid[0][i]
    
    for i in range(1, m):
        for j in range(n):
            if j > 0:
                left = dp[i-1][j-1]
            else:
                left = float("inf")
            if j < n-1:
                right = dp[i-1][j+1]
            else:
                right = float("inf")
            top = dp[i-1][j]
            dp[i][j] = min(left, right, top) + grid[i][j]
    
    return min(dp[-1])

grid = [[2,1,3],[6,5,4],[7,8,9]]

res = minimumFailingPathSum(grid)

print(res)