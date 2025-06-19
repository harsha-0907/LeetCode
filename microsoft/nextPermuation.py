

class Solution:
    def nextPermutation(self, arr):
        length = len(arr); breakingPoint = 0
        for i in range(length-1, 0, -1):
            if arr[i] > arr[i-1]:
                # Breaking ele is the i
                breakingPoint = i
                break
        # See what is the next biggest number from the reversed array
        if breakingPoint == 0:
            return arr.sort()

        print(breakingPoint)

        for i in range(breakingPoint, length):
            if arr[breakingPoint-1] > arr[i]:
                arr[breakingPoint-1], arr[i-1] = arr[i-1], arr[breakingPoint-1]
                arr[breakingPoint:] = sorted(arr[breakingPoint:])
                break

        else:
            arr[breakingPoint-1], arr[length-1] = arr[length-1], arr[breakingPoint-1]
            arr[breakingPoint:] = sorted(arr[breakingPoint:])
        
        return arr


obj = Solution()

arr = [1,3,2]

print(obj.nextPermutation(arr))