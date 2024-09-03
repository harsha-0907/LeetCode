# To find the minimum number of calculations to reach the target
from collections import deque

def minimumCalculations(start, end, array):
    MOD = 10**5
    shortest_distances = [float('inf')] * MOD
    shortest_distances[start] = 0
    #visited = {start}
    queue = deque([(start, 0)])
    
    while queue:
        node = queue.popleft()
        num, pos = node
        #print(num)
        if shortest_distances[num] != float("inf"):
            for ne in array:
                mul = (num * ne) % MOD
                if mul == end:
                    return pos + 1
                if shortest_distances[mul] > pos+1:
                    shortest_distances[mul] = pos + 1
                queue.append((mul, pos+1))
        
    return -1


start = 8
end = 4288
array = [20, 14, 1, 4, 20]
res = minimumCalculations(start, end, array)

print(res)
