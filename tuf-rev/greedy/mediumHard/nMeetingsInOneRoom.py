
class Solution:
    def maximumMeetings(self, start: list, end: list):
        number_of_meetings = len(start)
        meetings = sorted((end[i], start[i]) for i in range(number_of_meetings))
        cnt = 1; end_time, start_time = meetings.pop(0)
        for meet_end, meet_start in meetings:
            if meet_start > end_time:
                # This meeting can take place
                end_time = meet_end
                cnt += 1
            
        return cnt

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

ob = Solution()
print(ob.maximumMeetings(start, end))