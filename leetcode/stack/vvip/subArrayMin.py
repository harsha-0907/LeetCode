# to fund the sum of minimums of subarray

def minimumSubArrayBrute(array):
    def getSubArrays(array):
        total = 0
        for high in range(1, len(array)+1):
            for low in range(high):
                # print(array[low:high])
                total += min(array[low:high])
 
        return total
    total = getSubArrays(array)
    # print(total)
    return total

def minimumSubArrayBetterBrute(array):
    total = 0; mins = []
    for high in range(1, len(array)+1):
        for low in range(0, high-1):
            mins[low] = min(mins[low], array[high-1])
            total += mins[low]
        mins.append(array[high-1]); total += array[high-1]
    return total

def minimumSubArrayOptimal(array):
    length = len(array); total = 0
    min_num, min_pos = prev = array[-1], length-1
    for i in range(len(array)-1, -1, -1):
        if array[i] > min_num:
            this_total = (array[i] * (min_pos-i) + min_num*(length - min_pos))
        else:
            this_total = (array[i]*(length-i))
            min_num, min_pos = array[i], i
        print(array[i], "-", this_total)
        total += this_total
    return total

array = [11,81,94,43,3]

res = minimumSubArrayOptimal(array)

print(res)