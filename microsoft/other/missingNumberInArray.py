
class Solution:
    def minimumNumberInArray(self, arr: list):
        length = len(arr)
        expectedSum = ((length+1)*(length+2)) // 2
        return expectedSum - sum(arr)

obj = Solution()

print(obj.minimumNumberInArray([3,7,1,2,8,4,5]))