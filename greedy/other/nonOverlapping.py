# To find the non-overlapping intervals in the list of intervals

def nonOverlappingIntervals(intervals):
    """ To find the maximum number of non-overlapping intervals"""
    
    intervals.sort(key= lambda x: x[1])
    #print(intervals)
    length = len(intervals)
    pst, ped = intervals[0]; cnt = 0
    
    for pos in range(1, length):
        nst, ned = intervals[pos]
        if nst < ped:
            # Overlapping interval
            #print("Overlap", nst, ned)
            cnt += 1
        else:
            #print("N-Overlap", nst, ned)
            pst, ped = nst, ned
    
    return cnt
    

intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]

res = nonOverlappingIntervals(intervals)

print(res)