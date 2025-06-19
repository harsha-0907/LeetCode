
class Solution:
    def moveZeroesToEndBrute(self, arr):
        arr1 = [i for i in arr if i != 0]
        return arr1 + [0] * (len(arr) - len(arr1))
    
    def moveZeroesToEnd(self, arr):
        nonZeroPos = 0; length = len(arr)
        for i in range(length):
            if arr[i] != 0:
                arr[nonZeroPos], arr[i] = arr[i], arr[nonZeroPos]
                nonZeroPos += 1
        
        return arr

obj = Solution()
arr = [0,0,0,1,0,2,3,0]
print(obj.moveZeroesToEnd(arr))