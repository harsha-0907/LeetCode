# Finding the kth largest element
import heapq

class Solution:
    def quickSort(self, nums):
        length = len(nums)
        if length <= 1:
            return 0,  nums
        i, j = 0, length - 1
        pivot = nums[0]
        while i <= j:
            if nums[i] > pivot and nums[j] <= pivot:
                # Swap the 2 numbers
                nums[i], nums[j] = nums[j], nums[i]
                i += 1; j -= 1
            elif nums[i] > pivot and nums[j] > pivot:
                j -= 1
            elif nums[i] <= pivot and nums[j] <= pivot:
                i += 1
            else:
                j -= 1; i += 1
        
        nums[0], nums[j] = nums[j], nums[0]
        return j, nums

    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        for i in range(N):
            pos, nums = self.quickSort(nums)
            length = len(nums)
            pivot_pos = length - pos
            # print(pos, nums, pivot_pos, k)

            if pivot_pos == k:
                return nums[pos]
            elif pivot_pos < k:
                k -= pivot_pos
                # print("Left")
                nums = nums[:pos]
            else:
                # print("Right")
                nums = nums[pos+1:]
        
