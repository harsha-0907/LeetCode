
class Solution:
    # Finding the sub-array with the largest sum
    def maximumSubArrayBrute(self, arr):
        length = len(arr); maxTotal = 0
        for i in range(length):
            total = arr[i]
            if total < 0:
                continue
            for j in range(i+1, length):
                total += arr[j]
                if total > 0:
                    maxTotal = max(maxTotal, total)
        
        return maxTotal
    
    def maximumSubArrayOptimal(self, arr):
        length = len(arr); maxTotal = arr[0]; total = 0
        sumArray = [0]
        for ele in arr:
            total += ele
            sumArray.append(total)
        print(arr)
        print(sumArray)
        total = pos = 0; minEle = 0
        for ele in sumArray:
            if ele - minEle > maxTotal:
                maxTotal = ele - minEle
            minEle = min(minEle, ele)
        
        return maxTotal
    
    def maximumSubArray(self, arr):
        total = 0; maxTotal = arr[0]
        for ele in arr:
            total += ele
            maxTotal = max(total, maxTotal)
            if total < 0:
                total = 0
        
        return maxTotal

obj = Solution()

arr = [5, -2, 3, -1, 2]

print(obj.maximumSubArray(arr))