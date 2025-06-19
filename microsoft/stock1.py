

class Solution:
    def stock1Brute(self, arr):
        length = len(arr); maxProfit = 0
        for i in range(length):
            for j in range(i+1, length):
                profit = arr[j] - arr[i]
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
    
    def stock1(self, arr):
        minEle = arr[0]; maxProfit = 0
        for ele in arr:
            profit = ele - minEle
            if profit > maxProfit:
                maxProfit = profit
            minEle = min(minEle, ele)
        
        return maxProfit

obj = Solution()

arr = [7,1,5,3,6,4]

print(obj.stock1(arr))