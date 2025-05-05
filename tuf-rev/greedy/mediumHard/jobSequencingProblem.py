class Solution:
    def jobSequencing(self, deadlines, profits):
        def find(day):
            if parent[day] == day:
                return day
            parent[day] = find(parent[day])
            return parent[day]

        def union(x, y):
            parent[x] = y

        n = len(profits)
        max_deadline = max(deadlines)
        parent = [i for i in range(max_deadline + 1)]  # DSU parent array

        jobs = sorted(zip(profits, deadlines), reverse=True)
        total_profit = 0
        cnt = 0

        for profit, deadline in jobs:
            available_day = find(deadline)
            if available_day > 0:
                union(available_day, available_day - 1)
                total_profit += profit
                cnt += 1

        return cnt, total_profit


deadline = [4, 1, 1, 1]; profit = [20, 10, 40, 30]

obj = Solution()

print(obj.jobSequencing(deadline, profit))