# To merge the overlapping intervals into non-overlapping intervals

# THis is an alternative way to solve the insertInterval.(Actually much better way)

def mergeIntervals(intervals):
    """ To merge the intervals to make a group of non-overlapping intervals"""
    interals.sort(key=lambda x: x[0])
    length = len(intervals)
    output = []
    pst, ped = intervals[0]
    
    for pos in range(1, length):
        nst, ned = intervals[pos]
        if nst <= ped:
            # If the next interval starting is less than or equal to previous ending, it can be merged
            ped = max(ped, ned)
        else:
            # This is a seperate interval
            output.append([pst, ped])
            pst, ped = nst, ned
    
    output.append([pst, ped])
    return output

intervals = [[1,3],[2,6],[8,10],[15,18]]

res = mergeIntervals(intervals)    

print(res)       