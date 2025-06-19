

class Solution:
    def sumOf2Integers(self, arr, total):
        length = len(arr)
        for i in range(length):
            ele = arr[i]
            if total - ele in arr[i:]:
                return True
        return False

arr = [1,3,6,2]
obj = Solution()

print(obj.sumOf2Integers(arr, 8))