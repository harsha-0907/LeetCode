# To solve the problem of job-sequencing

def jobSequencing(jobs):
    """Job-Sequence is done using the greedy method
        1. Sort according to the value (1 priority), and then deadline
    """
    job_queue = set(); length = len(jobs); total = 0
    print(job_queue)
    
    jobs = [(jobs[i][2], jobs[i][1], jobs[i][0]) for i in range(length)]
    jobs = sorted(jobs, key= lambda x: -x[0])
    print(jobs)
    
    
    for value, deadline, job_id in jobs:
        if deadline not in job_queue:
            job_queue.add(deadline)
            total += value
        else:
            for limit in range(deadline, 0, -1):
                if limit not in job_queue:
                    job_queue.add(limit)
                    total += value
                    break
    
    return total
    
        
    
jobs = [[1,4,20],[2,1,1],[3,1,40],[4,1,30]]

res = jobSequencing(jobs)

print(res)