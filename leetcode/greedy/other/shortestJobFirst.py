# To implement the shortest first job approach and finding the total waiting time for the processes

def shortestJobFirst(jobs):
    jobs = sorted(jobs)
    waiting_time = total = 0; length = len(jobs)
    
    if length == 1:
        return 0
    else:
        # There are more than 1 jobs
        for i in range(length):
            total += (length-i-1) * jobs[i]
            
    return total // length

jobs = [1,2,3,4]
    
res = shortestJobFirst(jobs)

print(res)