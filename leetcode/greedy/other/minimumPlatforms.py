# To find the minimum number of platforms required for no waiting

def countMinimumPlatformsBrute(arr, dep):
    """ Not an optimal solution as we are considering updating the array everytime. T.C : O(n^2)"""
    def inMinutes(time):
        hrs = time // 100
        mins = time % 100
        return (hrs*60) + mins

    time = [0] * 1440; length = len(arr)
    
    for train in range(length):
        st, ed = inMinutes(arr[train]), inMinutes(dep[train])
        for i in range(st, ed):
            time[i] += 1
    
    return max(time)

def countMinimumPlatforms(arr, dep):
    arr[:] = sorted(arr); dep[:] = sorted(dep); length = len(arr)
    number_of_platforms = max_platforms = 0
        
    st = ed = 0
        
    while st < length:
        arr_time = arr[st]; dep_time = dep[ed]
        if arr_time <= dep_time:
            #print(arr_time, 'S')
            number_of_platforms += 1
            max_platforms = max(max_platforms, number_of_platforms)
            st += 1
        else:
            #print(dep_time, 'E')
            number_of_platforms -= 1
            ed += 1
        
    return max_platforms
        
    

arr = [900, 1100, 1235]
arr =  [900, 940, 950, 1100, 1500, 1800]
dep = [1000, 1200, 1240]
dep = [910, 1200, 1120, 1130, 1900, 2000]

res = countMinimumPlatforms(arr, dep)

print(res)