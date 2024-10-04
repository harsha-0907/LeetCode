# Must See

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


def makeSumDivisibleByk(arr, k):
    totalSum = sum(nums)
    rem = totalSum % p

    if rem == 0:
        return 0

    prefixMod = {0: -1}
    prefixSum = 0
    minLength = len(nums)

    for i, num in enumerate(nums):
        prefixSum += num
        currentMod = prefixSum % p
        targetMod = (currentMod - rem + p) % p

        if targetMod in prefixMod:
            minLength = min(minLength, i - prefixMod[targetMod])

        prefixMod[currentMod] = i

    return minLength if minLength < len(nums) else -1    



arr = [1,2,3]
k = 6

res = makeSumDivisibleByK(arr, k)

print(res)