

class Solution:
    def longestConsecutiveBrute(self, arr):
        arr.sort(); length = len(arr)
        maxLength = 0; leng = 1
        for pos in range(1, length):
            if arr[pos] - arr[pos-1] == 1:
                leng += 1
                maxLength = max(maxLength, leng)
            elif arr[pos] == arr[pos-1]:
                pass
            else:
                leng = 1

        return maxLength
    
    def longestConsecutive(self, arr):
        reqd = set(arr)
        count = 1; maxCount = 0; done = set()
        for ele in arr:
            if ele in done:
                continue
            done.add(ele)
            e = ele - 1; count = 1
            while e in reqd:
                count += 1
                e -= 1
                done.add(e)
            e = ele + 1
            while e in reqd:
                count += 1
                e += 1
                done.add(e)
            maxCount = max(maxCount, count)
        
        return maxCount
            

obj = Solution()

arr = [1,0,1,2]

print(obj.longestConsecutive(arr))