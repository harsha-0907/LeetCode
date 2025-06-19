

class Solution:
    def threeSumBrute(self, arr, total):
        length = len(arr); setOfAnswers = set()
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if arr[i] + arr[j] + arr[k] == total:
                        setOfAnswers.add(tuple(sorted([arr[i], arr[j], arr[k]])))
        
        return setOfAnswers
    
    def threeSumLittleOptimal(self, arr, total):
        arr.sort(); length = len(arr)
        ans = []
        for i in range(length):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1, length):
                if j != i+1 and arr[j] == arr[j-1]:
                    continue
                for k in range(j+1, length):
                    if k != j+1 and arr[k] == arr[k-1]:
                        continue
                    if arr[i] + arr[j] + arr[k] == total:
                        ans.append((arr[i], arr[j], arr[k]))
        return ans

    def threeSum(self, arr, total):
        arr.sort(); ans = []; length = len(arr)
        for i in range(length):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            j = i + 1; k = j + 1
            while k < length and arr[i] + arr[j] + arr[k] <= total:
                k += 1
            while j < k:
                tot = arr[i] + arr[j] + arr[k]
                if tot == total:
                    ans.append((arr[i], arr[j], arr[k]))
                    break
                elif tot < total:
                    j += 1
                else:
                    k -= 1
        return ans

obj = Solution()

arr = [-1,0,1,2,-1,-4]
k = 0

print(obj.threeSum(arr, k))
                    