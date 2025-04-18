# Check if a given arrray is a valid heap or not

class Solution:
    def isHeap(self, nums):
        length = len(nums)
        for i in range((length // 2) + 1):
            if not self.checkHeap(nums, i, (i*2)+1, (i*2)+2):
                return False
        
        return True

    def checkHeap(self, nums, parent_pos, child_a_pos, child_b_pos):
        child_a = float("inf") if child_a_pos >= len(nums) else nums[child_a_pos]
        child_b = float("inf") if child_b_pos >= len(nums) else nums[child_b_pos]
        
        if nums[parent_pos] <= child_a and nums[parent_pos] <= child_b:
            return True
        return False
        
nums = [10, 20, 30, 25, 15]

sol = Solution()

print(sol.isHeap(nums))