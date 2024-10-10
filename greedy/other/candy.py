# To solve the candy problem


def distributeCandies(children):
    """ To distribute the minimum number of candies to the children following the given rules"""
    # Here the difficulty is to assign the number of candies while descent or ascent for that we are travesing through the
    # array twice (forward & backward) to make sure that both the ascent & descent cases are considered
    candies = [0 for child in children]; length = len(children)
    candies[0] = 1
    
    for pos in range(1, length):
        if children[pos] > children[pos-1]:
            candies[pos] = candies[pos-1] + 1
        else:
            candies[pos] = 1
    
    candies[-1] = max(candies[-1], 1)
    for pos in range(length-2, -1, -1):
        if children[pos] > children[pos+1]:
            candies[pos] = max(candies[pos+1]+1, candies[pos])
    
    return candies, sum(candies)

ratings = [1,2,2]

res = distributeCandies(ratings)

print(res)