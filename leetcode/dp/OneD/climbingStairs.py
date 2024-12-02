# The climbing staris problem
# Here, we are trying to find the number of possiblities to reach nth step by either 1/2 steps at a time

def countingStars(n):
    def countingSteps(n):
        # We know that the number of steps to climb 1 step is -> 1
        # We also know that to climb 2 steps is 2 (1+1 or 2 at a time)
        
        if arr[n] != -1:
            return arr[n]
        arr[n] = countingSteps(n-1) + countingSteps(n-2)
        return arr[n]
        
    arr = [-1 for i in range(n+1)]
    arr[0] = 0; arr[1] = 1; arr[2] = 2

    return countingSteps(n)

res = countingStars(3)
print(res)
        