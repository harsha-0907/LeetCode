

class Solution:
    def longestSubArrayWithGivenSumK(self, arr, k):
        total = 0; sumArray = []; dict1 = dict(); pos = 0; maxLength = 0
        for i in arr:
            total += i
            if total == k:
                maxLength = pos + 1
            if total not in dict1:
                dict1[total] = pos
            if total - k in dict1:
                maxLength = max(maxLength, pos - dict1[k-total] + 1)
            sumArray.append(total)
            pos += 1
        return maxLength

obj = Solution()
arr = [1,2,1,1,1]
k = 3

print(obj.longestSubArrayWithGivenSumK(arr, k))