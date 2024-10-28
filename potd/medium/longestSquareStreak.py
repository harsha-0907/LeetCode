# To find the longest streak of numbers that have squares

from typing import Optional

def findLongestStreak(nums: Optional[list]=[]):
    nums1 = set(nums)
    sq_nums = {num**2 for num in nums}
    common_nums = list(sorted(nums1.intersection(sq_nums)))
    
    # We have found the common numbers that are present in both the array (Squares)
    maxsize = 0
    while len(common_nums) > 0:
        num = common_nums[0]; size = 1
        _num = num**2
        while _num in common_nums:
            size += 1
            common_nums.remove(_num)
            _num = _num**2
        common_nums.remove(num)
        maxsize = max(maxsize, size+1)
        
    return maxsize
    
nums = [2,3,5,6,7]  

res = findLongestStreak(nums)

print(res)