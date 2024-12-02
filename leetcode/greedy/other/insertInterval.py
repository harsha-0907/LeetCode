# To insert an interval into existing non-overlapping intervals

# Made this very complex and non-completing
def insertIntervalBrute(intervals, new_interval):
    sflag = True; pos = 0; length = len(intervals)
    start, end = new_interval
    
    for pos in range(length):
        st, ed = intervals[pos]
        if (start >= st and start < ed) or (st > start and end > st):
            #The interval starts from here
            intervals[pos][0] = min(st, start)
            if ed >= end:
                # The new interval only requires modification of the existing interval
                return intervals
            else:
                if pos == length-1:
                    # This is the last element
                    intervals[pos][1] = end
                    return intervals
                else:
                    # There are still intervals after the pos
                    ipos = pos
                    #print(intervals,ipos)
                    for pos in range(ipos, length):
                        st = intervals[pos][0]
                        if st > end:
                            pos -= 1
                            intervals[ipos][1] = max(end, intervals[pos][1])
                            break
                    else:
                        # No elements are remaining
                        #print(ipos, intervals)
                        print(intervals[ipos])
                        intervals[ipos][1] = end
                        return intervals[:ipos+1]
                    
                    # There are elements still existing
                    return intervals[:ipos+1] + intervals[pos+1:]
    
    return -1   # Impossoble case


def insertInterval(intervals, newInterval):
    output = []

    newStart = newInterval[0]
    newEnd = newInterval[1]

    i = 0
    n = len(intervals)

    # Add all intervals that come before the new interval
    while i < n and newStart > intervals[i][0]:
        output.append(intervals[i])
        i += 1

    # Merge newInterval with the last interval in output if necessary
    if not output or output[-1][1] < newStart:
        output.append(newInterval)
    else:
        output[-1][1] = max(output[-1][1], newEnd)

    # Add remaining intervals, merging if necessary
    while i < n:
        start, end = intervals[i]
        if output[-1][1] < start:
            output.append([start, end])
        else:
            output[-1][1] = max(output[-1][1], end)
        i += 1

    return output

intervals = [[1,3],[6,9]]
new_interval = [2,5]

res = insertInterval(intervals, new_interval)

print(res)