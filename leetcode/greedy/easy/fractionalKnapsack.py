# This is the fractional knapsack problem 

def fractionalKnapsack(max_weight, arr, n):
    for ele in arr:
        ele.value = ele.value / ele.weight
    arr = sorted(arr, reverse=True, key=lambda s: s.value)
    print(arr)

    tot_weight = 0; tot_value = 0

    for ele in arr:
        if ele.weight + tot_weight < max_weight:
            dif = max_weight - tot_weight
            addValue = ele.value * dif
            break
        else:
            tot_weight += ele.weight
            tot_value += (ele.value * ele.weight)
    
    return tot_weight


class Item:

    def __init__(self, val, w):
        self.value = val
        self.weight = w

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, w = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(w, arr, n))
