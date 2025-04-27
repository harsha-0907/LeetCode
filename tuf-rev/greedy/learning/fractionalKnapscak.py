class Solution:
    def fractionalknapsack(self, val: list, wt: list, capacity):
        length = len(val); value = 0
        density = sorted([(val[i]/wt[i], wt[i]) for i in range(length)], reverse=True)
        for item in density:
            if capacity <= 0:
                break
            den, wt = item
            weight_added = min(capacity, wt)
            value += weight_added * den; capacity -= weight_added
        
        return value


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read values array
        values = list(map(int, input().strip().split()))

        # Read weights array
        weights = list(map(int, input().strip().split()))

        # Read the knapsack capacity
        W = int(input().strip())

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(values, weights, W))
        print("~")

        """ 
        60 100 120
10 20 30
50
        """