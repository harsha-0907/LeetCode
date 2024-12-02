# The House-Robber Problem

def houseRobber(houses):
    n = len(houses)
    # The option to choose the present house depends on the total obtained from the previous houses
    if n == 1:
        return houses[0]
    array = [0 for i in range(n)]
    array[0] = houses[0]; array[1] = max(houses[0], houses[1])
    for i in range(2, n):
        array[i] = max(array[i-1], array[i-2]+houses[i])
    
    #print(array)
    return array[-1]

houses = [2, 1, 1, 2]
res = houseRobber(houses)

print(res)