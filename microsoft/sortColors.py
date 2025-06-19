
class Solution:
    def sortColorsBrute(self, arr):
        arr.sort()
        return arr
    
    def sortColors(self, arr):
        length = len(arr)
        c0 = c1 = c2 = 0
        for i in range(length):
            if arr[i] == 0:
                c0 += 1
            elif arr[i] == 1:
                c1 += 1
            elif arr[i] == 2:
                c2 += 1
        for i in range(length):
            if i < c0:
                arr[i] = 0
            elif i < c0 + c1:
                arr[i] = 1
            elif i < c0 + c1 + c2:
                arr[i] = 2
        return arr


obj = Solution()
arr = [2,0,2,1,1,0]

print(obj.sortColors(arr))