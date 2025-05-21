

from typing import List
import heapq

class Solution:
    def averageTimes(self, n : int, arrivalTimes : List[int], burstTimes : List[int]) -> List[float]:
        length = len(arrivalTimes); mainHeap = []; timeHeap = []
        total_waiting_time = total_turnaround_time = 0
        for i in range(length):
            heapq.heappush(mainHeap, (arrivalTimes[i], burstTimes[i]))
        
        current_time = 0; completed_jobs = []
        while len(completed_jobs) < length:
            while mainHeap and mainHeap[0][0] <= current_time:
                heapq.heappush(timeHeap, heapq.heappop(mainHeap)[::-1])
                
            if not timeHeap:    # This means that the next job arrives afer the completion of all jobs in timeHeap
                current_time = mainHeap[0][0]
                continue    # We wait till the arrival of the next jobs(idle state)
            
            job = heapq.heappop(timeHeap)
            burst_time, arr_time = job
            print(arr_time, burst_time)
            completed_jobs.append((arr_time, burst_time, current_time))
            waiting_time = current_time - arr_time; turnaround_time = current_time + burst_time - arr_time
            total_waiting_time += waiting_time; total_turnaround_time += turnaround_time
            current_time += burst_time

        return [round(total_waiting_time / length, 2), round(total_turnaround_time / length, 2)]


obj = Solution()
input_data = """
9
4 4 9 9 1 0 6 7 8
5 3 1 3 6 1 1 5 6
"""

input_data = input_data.split("\n")
n, arrivalTimes, burstTimes = int(input_data[1]), [int(i) for i in input_data[2].split()], [int(i) for i in input_data[3].split()]
# print(n, arrivalTimes, burstTimes)
result = None
result = obj.averageTimes(n, arrivalTimes, burstTimes)
print(result)