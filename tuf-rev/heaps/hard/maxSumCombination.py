import heapq

class Solution:
    def maxCombinationsBrute(self, N, K, A, B):
        # Code here
        A, B = sorted(A, reverse=True), sorted(B, reverse=True)
        cnt = 0; total = []
        for ele1 in A:
            for ele2 in B:
                heapq.heappush(total, -(ele1 + ele2))
        return [-heapq.heappop(total) for i in range(K)]
    
    def maxCombinationsOptminal(self, N, K, A, B):
        A, B = sorted(A, reverse=True), sorted(B, reverse=True)
        A, B = sorted(A, reverse=True), sorted(B, reverse=True)
        i, j = 0, 0; positions = set(); cnt = 0; arr = [(-1 * (A[0]+B[0]), (0, 0))]
        ans = []; cnt = 0
        while cnt < K:
            total, pos = heapq.heappop(arr)
            if pos not in positions:
                positions.add(pos)
            else:
                continue
            i, j = pos
            heapq.heappush(ans, total)
            if i < N-1 and j < N-1:
                heapq.heappush(arr, (-1*(A[i+1] + B[j]), (i+1, j)))
                heapq.heappush(arr, (-1*(A[i] + B[j+1]), (i, j+1)))
            cnt += 1
        return [-heapq.heappop(ans) for i in range(K)]
        
            