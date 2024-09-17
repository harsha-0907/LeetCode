#Also called the GeekJump 
# Here we use the memoization technique to solve this problem

def geekJump(arr):
    # To jump to the n-1 th element from the 1st element
    n = len(arr)
    if n == 1:
        return 0
    elif n == 2:
        return abs(arr[1]- arr[0])
    else:
        dist = [0 for i in range(n)]
        dist[0] = 0
        dist[1] = abs(arr[1] - arr[0])
        # TO reach the nth step we need to check the minimum of n-1 th + next step or n-2th step + next step
        def calculateDistance(n):
            if dist[n] != 0:
                return dist[n]
            else:
                dist[n] = min(calculateDistance(n-1)+abs(arr[n]-arr[n-1]), calculateDistance(n-2)+abs(arr[n]-arr[n-2]))
                return dist[n]
        
        return calculateDistance(n-1)

arr = [10, 20, 30, 10]
res = geekJump(arr)

print(res)