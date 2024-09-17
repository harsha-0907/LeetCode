# Fibonacci Numbers using Bottom-Up and To-Down Approach

def bottomUp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        n -= 1
        first = 0; second = 1
        for i in range(n):
            third = first + second
            first, second = second, third
        
        return third

def topDown(n):
    # To follow the top-down approach
    dict1 = {0: 0, 1: 1}
    def fib(i):
        if i in dict1:
            return dict1[i]
        else:
            ans = fib (i-1) + fib(i-2)
            dict1[i] = ans
            return ans
    
    return fib(n)

n = 1
print(bottomUp(n))
print(topDown(n))