# Minimal Cost (Extension of Frog-Jump)

def frogJump2(arr, k):
    # Using Tabulation method
    n = len(arr)
    dict1 = {0: 0}
    for i in range(1, n):
        mindist = 1000001
        d = max(0, i-k)
        for j in range(d, i):
            #print(i, j)
            if j >= 0:
                #print(i, j, dict1[j])
                mindist = min((dict1[j] + abs(arr[i] - arr[j])), mindist)
                #print(mindist)
        dict1[i] = mindist
    
    #print(dict1)
    return dict1[n-1]

arr = [10, 20, 10]
k = 1

res = frogJump2(arr, k)

print(res)

