

class Solution:
    def fourSumBrute(self, arr, total):
        length = len(arr); pairs = []
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    for l in range(k+1, length):
                        if arr[i] + arr[j] + arr[k] + arr[l] == total:
                            newPair = sorted(arr[i], arr[j], arr[k], arr[l])
                            if newPair not in pairs:
                                pairs.append(newPair)
        return pairs
    
    def fourSum(self, arr, total):
        length = len(arr); ans = []
        for i in range(length):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1, length-1):
                if j != i+1 and arr[j] == arr[j-1]:
                    continue
                
                k = j + 1; l = length-1
                while k < l:
                    if k != j+1 and arr[k] == arr[k-1]:
                        k += 1; continue
                    if l != length-1 and arr[l] == arr[l+1]:
                        l -= 1; continue
                    tot = arr[i] + arr[j] + arr[k] + arr[l]
                    if tot == total:
                        ans.append((arr[i], arr[j], arr[k], arr[l]))
                        k += 1; l -= 1
                    elif tot > total:
                        l -= 1
                    else:
                        k += 1
        
        return ans
    
    

obj = Solution()
arr = []
total = 0

print(obj.fourSum(arr, total))