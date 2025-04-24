import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k; length = len(nums)
        self.nums = [-i for i in nums]
        heapq.heapify(self.nums)
        self.kLargest = []
        for i in range(min(k, length)):
            ele = heapq.heappop(self.nums)
            heapq.heappush(self.kLargest, -ele)

    def add(self, val: int) -> int:
        heapq.heappush(self.kLargest, val)

        if len(self.kLargest) > self.k:
            heapq.heappop(self.kLargest)
        elif len(self.kLargest) == self.k:
            pass
        else:
            return None
        
        return self.kLargest[0]