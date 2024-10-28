# To find the smallest range of numbers 

# This is the optimized brute force approach (not at all recommended)
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def binarySearch(target, arr):
            low, high = 0, len(arr)-1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        
        def searchLimit(limit, arr):
            # We will return true if there exists an element 
            # print("Target - ", limit[0], "Max - ", limit[1])
            for arr in nums:
                pos = binarySearch(limit[0], arr)
                if pos == len(arr):
                    return False
                elif arr[pos] == limit[0]:
                    continue
                elif pos == -1:
                    if arr[0] > limit[0] and arr[0] <= limit[1]:
                        continue
                    else:
                        return False
                elif pos == len(arr)-1:
                    if arr[pos] > limit[0] and arr[pos] <= limit[1]:
                        continue
                else:
                    if arr[pos+1] > limit[0] and arr[pos+1] <= limit[1]:
                        continue
                return False
            
            return True

        dict1 = set(); length = len(nums)
        minst = mined = 10000; maxst = maxed = -1000000
        for pos in range(length):
            num = nums[pos]
            minst = min(minst, num[0]); mined = min(mined, num[-1])
            maxst = max(maxst, num[0]); maxed = max(maxed, num[-1])
            for n in num:
                if n not in dict1:
                    dict1.add(n)
        
        numbers = sorted(list(dict1)); length = len(numbers)
        minlen, limit = min(maxst-minst, maxed-mined), (minst, maxst) if (maxst - minst) <= (maxed-mined) else (mined, maxed)
        lpos, hpos = 0, binarySearch(maxst, numbers); h1 = hpos
        while lpos < length and numbers[lpos] <= maxed:
            for hpos in range(lpos, length):
                rng = numbers[hpos] - numbers[lpos]
                if rng >= minlen:
                    break
                else:
                    r = searchLimit((numbers[lpos], numbers[hpos]), nums)
                    if r:
                        if minlen > rng:
                            limit = (numbers[lpos], numbers[hpos])
                            minlen = rng   
            lpos += 1
        return limit        

def findSmallestRangeUsingHeap(nums):
    min_heap = []
    current_max = float('-inf')
        
    # Initialize heap with the first element from each subarray
    for i in range(len(nums)):
        heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, array index, element index)
        current_max = max(current_max, nums[i][0])
        
    smallest_range = float('inf'), -1, -1
        
    while min_heap:
        current_min, list_index, element_index = heapq.heappop(min_heap)
        
        # Update the smallest range
        if current_max - current_min < smallest_range[0]:
            smallest_range = (current_max - current_min, current_min, current_max)
            
        # If we've reached the end of one of the subarrays, break
        if element_index + 1 == len(nums[list_index]):
            break
            
        # Push the next element from the same list into the heap
        next_element = nums[list_index][element_index + 1]
        heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
        current_max = max(current_max, next_element)
        
    return [smallest_range[1], smallest_range[2]]

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

res = findSmallestRange(nums)

print(res)