# The DP-2D Array problem

def geekTraining(days):
    def calculateWork(day):
        nonlocal max1, max2
        dict1 = dict()
        for i in range(3):
            d1 = day[i]
            if i != max1[1]:
                d1 = day[i] + max1[0]
            if i != max2[1]:
                d1 = max(d1, day[i] + max2[0])
            dict1[i] = d1
        #print(dict1)
        m = sorted(dict1.values())[1:]
        print(m)
        if m[0] != m[1]:
            for i in dict1:
                if dict1[i] == m[0]:
                    max2 = [dict1[i], i]
                if dict1[i] == m[1]:
                    max1 = [dict1[i], i]
        else:
            for i in dict1:
                if dict1[i] == m[1]:
                    max1 = [dict1[i], i]
                    del(dict1[i])
                    break
            for i in dict1:
                if dict1[i] == m[0]:
                    max2 = [dict1[i], i]
        return max1, max2
    n = len(days)
    max1 = [0, -1]; max2 = [0, -1]
    for i in range(n):
        max1, max2 = calculateWork(days[i])
        print(max1, max2)
    
    return max(max1[0], max2[0])


arr = [[7, 6, 1], [3, 9, 7], [1, 3, 5], [9, 7, 6], [1, 10, 1], [1, 7, 2], [4, 9, 10], [4, 5, 5], [7, 1, 7], [7, 2, 9]]
res = geekTraining(arr)


print(res)