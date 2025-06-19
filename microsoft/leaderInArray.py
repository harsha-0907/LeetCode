

class Solution:
    def leaderInArray(self, arr):
        arr.reverse(); length = len(arr); maxEle = arr[0]
        leaders = [arr[0]]
        for i in range(1, length):
            if arr[i] > maxEle:
                leaders.append(arr[i])
                maxEle = arr[i]
            
        leaders.reverse()

        return leaders

obj = Solution()

arr = [10, 22, 12, 3, 0, 6]

print(obj.leaderInArray(arr))