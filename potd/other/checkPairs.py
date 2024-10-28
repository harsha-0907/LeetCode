# Check if the array pairs are sorted into order of 2 that are divisible
from collections import deque

def checkPairs(arr, k):
    def calculateDifference(num, k):
        if num > k:
            return k-(num%k)
        else:
            return k- num
    
    dp = deque(); dcnt = 0; maxele = 0
    for ele in arr:
        if ele % k==0:
            dcnt += 1
        else:
            dp.append(ele%k)
    
    print(dp)
    dp1 = dp.copy()
    if dcnt % 2:
        # If the number of pairs that are divisble by k are odd -> return True(div + !div) -> !div
        return False
    
    for ele in dp:
        if ele not in dp1:
            continue
        dif = calculateDifference(ele, k)
        print(ele, dif)
        if dif not in dp1:
            return False
        dp1.remove(ele); dp1.remove(dif)

    return True

arr = [1,2,3,4,5,10,6,7,8,9]
k = 5

res = checkPairs(arr, k)

print(res)