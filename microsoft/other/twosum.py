

class Solution:
    def twoSumBrute(self, arr, k):
        length = len(arr)
        for i in range(length):
            for j in range(i+1, length):
                if arr[i] + arr[j] == k:
                    return (arr[i], arr[j])
        return None
    
    def twoSum(self, arr, k):
        arr.sort(); length = len(arr)
        i,j = 0, length-1
        for j in range(length):
            tot = arr[i] + arr[j]
            if tot == k:
                return (arr[i], arr[j])
            elif tot > k:
                break
        
        while i < j:
            tot = arr[i] + arr[j]
            if tot > k:
                j -= 1
            elif tot < k:
                i += 1
            else:
                return (arr[i], arr[j])
        return None


obj = Solution()
arr = [2,7,11,15]
k = 26

print(obj.twoSum(arr, k))