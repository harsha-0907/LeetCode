import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = dict(); arr = []
        for ele in nums:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1
        
        for ele, cnt in dict1.items():
            heapq.heappush(arr, (-cnt, ele))
        
        ans = []
        for i in range(min(k, len(arr))):
            cnt, ele = heapq.heappop(arr)
            ans.append(ele)
        return ans