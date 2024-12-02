# To find the maximum number of meetings that can be accomodated in 1 meeting room


def numberOfMeetings(start, end):
    """To find the maximum number of meetings that can be held in one single room"""
    length = len(start)
    
    meetings = [(start[i], end[i]) for i in range(length)]
    meetings[:] = sorted(meetings, key=lambda x: x[1])
    
    print(meetings); ed = -1; cnt = 0
    
    for pos in range(length):
        if meetings[pos][0] > ed:
            ed = meetings[pos][1]
            cnt += 1
        
    return cnt


start = [1, 3, 0, 5, 8, 5]

end = [2, 4, 6, 7, 9, 9]
    
res = numberOfMeetings(start, end)

print(res)