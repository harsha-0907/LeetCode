# To find the kth smallest lexicographical number in the series
# The proposed solution(by me) has time complexity O(n) which is not feasible for this question
# They require a O(log(n)) time complexity solution

def kthSmallestLexicographicalSeries(n, k):
    def series(start, cnt):
        nonlocal ans
        start *= 10
        for i in range(10):
            if i+start > n:
                return cnt
            cnt += 1
            if cnt == k:
                ans = start + i
                return cnt
            cnt = series(start+i, cnt)
            if ans != -1:
                return cnt
    if k > n:
        return -1
    ans = -1
    cnt = 0; start = 1; num = -1
    for start in range(1, 10):
        cnt += 1
        # Here since 'k' <= 'n we can 
        if cnt == k:
            return start
        cnt = series(start, cnt)
        if ans != -1:
            return ans

res = kthSmallestLexicographicalSeries(1, 1)

print(res)