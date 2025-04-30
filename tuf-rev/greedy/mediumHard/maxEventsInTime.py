import heapq

class Solution:
    def maxEvents(self, events: list) -> int:
        number_of_events = len(events); pos = 0
        events.sort(); minHeap = []

        while pos < number_of_events:
            i = pos
            while i == pos:
                heapq.heappush(minHeap, events[i][1])

            



events = [[27,27],[8,10],[9,11],[20,21],[25,29],[17,20],[12,12],[12,12],[10,14],[7,7],[6,10],[7,7],[4,8],[30,31],[23,25],[4,6],[17,17],[13,14],[6,9],[13,14]]
ob = Solution()

print(ob.maxEvents(events))