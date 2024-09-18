# House-Robber-II
# Here on top of the House-Robber problem we now know that the first and last vertices are connected

def houseRobber2(houses):
    if len(houses) == 1:
        return houses[0]
    elif len(houses) == 2:
        return max(houses)
    else:
        n = len(houses)
        # For the houses from 1 to n-1
        n1 = houses[0]; n2 = max(houses[1], houses[0])
        for i in range(2, n-1):
            n3 = max(n1 + houses[i], n2)
            n1, n2 = n2, n3
        # Storing the first result in f1
        f1 = n2

        # For the houses from 2 to n
        n1 = houses[1]; n2 = max(houses[1], houses[2])
        for i in range(3, n):
            n3 = max(n1 + houses[i], n2)
            n1, n2 = n2, n3
        # Storing the result in f2
        f2 = n2
        return max(f1, f2)

houses = [1,2,3]

res = houseRobber2(houses)

print(res)