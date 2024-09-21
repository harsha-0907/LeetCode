# Generate the first 'n' numbers in lexicographical order
from collections import deque

def generateSeries(n):
    def getSeries(start):
        start *= 10
        for i in range(10):
            if i + start > n:
                break
            series.append(i+start)
            getSeries(i+start)
        
    start = 1; series = deque()
    for start in range(1, 10):
        if start <= n:
            series.append(start)
            getSeries(start)

    return series
res = generateSeries(2)

print(res)