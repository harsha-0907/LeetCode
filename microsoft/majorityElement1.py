
class Solution:
    def majorityElement2Brute(self, arr):
        dict1 = dict(); length = len(arr)
        for ele in arr:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1
        
        for ele in dict1:
            if dict1[ele] > length // 2:
                return ele
        return None
    
    def majorityElement2(self, arr):
        majEle = arr[0]; count = 0
        for ele in arr:
            if ele == majEle:
                count += 1
            elif count > 0:
                count -= 1
            else:
                majEle = ele; count = 1
        if arr.count(majEle) > len(arr) // 2:
            return majEle        
        return None

obj = Solution()
arr = [2, 2, 1, 1, 1, 2, 2]

print(obj.majorityElement2(arr))