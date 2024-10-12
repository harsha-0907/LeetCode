# To divide the intervals into non-overlapping groups of intervals

# The not so good method
def divideIntervalsBrute(intervals):
    """ Here we will divide the interval by first sorting them in ascending order, then
    take an interval and check if it fits into any existing interval groups else, we will create a new group"""
    
    intervals.sort(key= lambda x: x[0])
    max_intervals = 0
    groups = []  # The format of the group will be (st, ed)
        
    for start, end in intervals:
        for pos in range(len(groups)):
            st, ed = groups[pos]
            if start > ed:
                groups[pos][1] = end
                break
        else:
            groups.append([start, end])    
    return len(groups)

# This is a lot optimized
def divideIntervals(intervals):
    length = len(intervals)
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)

    pos = end_pos = groups = max_groups = 0
    while pos < length:
        ed = end[end_pos]; st = start[pos]
        if st <= ed:
            groups += 1; pos += 1
            max_groups = max(max_groups, groups)
        else:
            groups -= 1
            end_pos += 1
        
    return max_groups

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

res = divideIntervals(intervals)

print(res)