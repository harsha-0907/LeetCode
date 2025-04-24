import heapq
class Solution:
   def minCost(self, arr):
    # code here
    heapq.heapify(arr)
    
    total = 0
    while len(arr) > 1:
        ele1 = heapq.heappop(arr)
        ele2 = heapq.heappop(arr)
        total += ele1 + ele2
        heapq.heappush(arr, ele1+ele2)
    
    return total