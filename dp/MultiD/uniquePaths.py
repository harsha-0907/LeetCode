# To find the unique paths to travel from (0, 0) to (n-1, n-1) in a matrix

def calculateUniquePaths(m, n):
    # To calculate the total number of unique paths
    # Let the number of ways to reach (i, j) = F(i, j)
    # The number of ways to reach F(i, j) = F(i-1, j) + F(i, j-1)
    # Let all the different ways to reach any position be 0 initially

    dict1 = dict()
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dict1[(i, j)] = 1
            else:
                dict1[(i, j)] = (dict1[(i-1),j] + dict1[(i, j-1)])
    
    print(dict1)
    return dict1[(m-1, n-1)]


#m, n = [int(i) for i in input().split()]
m = 2; n =3

res = calculateUniquePaths(m, n)

print(res)