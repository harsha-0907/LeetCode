
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = 0; length = len(intervals)
        newst = newed = None
        st, ed = newInterval
        if ed >= intervals[0][0] and ed <= intervals[0][1]:
            intervals[0][0] = st
            return intervals
        if ed < intervals[0][0]:
            intervals.insert(0, (st, ed))
            return intervals
        
        for pos in range(length):
            if intervals[pos][0]  <= st and intervals[pos][1] >= ed:
                return intervals
            elif intervals[pos][0] <= st and intervals[pos][1] > st:
                newst = intervals[pos][0]
                break
            elif intervals[pos][0] > st:
                continue
        else:
            newst = st
        print(newst); print(pos)
        ipos = pos
        for i in range(pos, length):
            if intervals[i][0] > ed:
                newed = ed
                break
            elif intervals[i][0] <= ed and intervals[i][1] >= ed:
                newed = intervals[i][1]
                pos += 1
                break
        else:
            newed = ed
        print(newed, ipos, i)
        for j in range(ipos, i+1):
            print(intervals.pop(ipos))
        intervals.insert(ipos, [newst, newed])
        
        return intervals

obj = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(intervals)
print(obj.insert(intervals, newInterval))