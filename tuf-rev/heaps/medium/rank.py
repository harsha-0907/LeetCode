# Ranking the numbers present in an array

class Solution:
    def rankAlgorithm(self, arr):
        arr1 = sorted(arr); arr2 = dict()
        rank = 1
        for ele in arr1:
            if ele not in arr2:
                arr2[ele] = rank
                rank += 1
        return [arr2[ele] for ele in arr]

arr = [9,8,7,6,5,4,3,2,1,0]
ob = Solution()
print(ob.rankAlgorithm(arr))