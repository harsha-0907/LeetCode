# To find the smallest sum till the end of the triangle 
# To find the smallest sum of all the levels in the triangle


def smallestSumTriangle(triangle):
    n = len(triangle)
    dp = [[float("inf") for j in range(i)] for i in range(1, n+1)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    return min(dp[-1])

arr = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = smallestSumTriangle(arr)

print(res)