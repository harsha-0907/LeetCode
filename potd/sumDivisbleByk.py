# To find the least size of sub-array to be removed to make it divisible by 'k'

# TLE
def makeSumDivisibleByK(arr, k):
    sumarray = [0]; tot = 0
    for ele in arr:
        tot += (ele % k)
        sumarray.append(tot)
    
    rem = tot % k
    if rem == 0:
        return 0
    minlen = len(arr)
    for pos in range(1, len(sumarray)):
        for j in range(pos):
            t = sumarray[pos] - sumarray[j]
            if t % k == rem:
                minlen = min(minlen, (pos - j))
    
    if minlen == len(arr):
        return -1
    return minlen


arr = [1,2,3]
k = 6

res = makeSumDivisibleByK(arr, k)

print(res)