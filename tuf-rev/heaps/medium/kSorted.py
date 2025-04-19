# Sorting k distant sorted elements
import heapq
class Solution:
    def nearlySortedInsertionSort(self, arr, k):
        length = len(arr); pos = None
        for i in range(length):
            pos = i
            for j in range(i+1, i+k+1):
                if j >= length:
                    break
                elif arr[pos] >= arr[j]:
                    pos = j
            arr[i], arr[pos] = arr[pos], arr[i]
        return arr

    def nearlySortedUsingBinarySearch(self, arr, k):
        def binaryInsert(ele, length):
            i, j = 0, length
            while i <= j:
                mid = (i+j) // 2
                if arr[mid] == ele:
                    # Shift the elements towards right
                    arr[mid+1:pos+1] = arr[mid:pos]
                    arr[mid] = ele
                elif arr[mid] < ele:
                    i = mid + 1
                else:
                    j = mid - 1
            arr[i+1:pos+1] = arr[i:pos]
            arr[i] = ele
            
        sortedList = []
        arr[:k+1] = sorted(arr[:k+1])

        for pos, ele in enumerate(arr[k+1:]):
            binaryInsert(ele, pos+k)
        
        return arr

    def nearlySortedUsingMinHeap(self, arr, k):
        minHeap = []; length = len(arr)
        for i in range(k):
            heapq.heappush(minHeap, arr[i])
        
        for i in range(length):
            if i + k < length:
                ele = arr[i + k]
                heapq.heappush(minHeap, ele)

            ele = heapq.heappop(minHeap)
            arr[i] = ele
    
        return arr

arr = [10, 9, 7, 8, 4, 70, 60, 50]
k = 4
ob = Solution()
print(ob.nearlySortedUsingMinHeap(arr, k))