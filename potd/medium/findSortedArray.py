# Check if the array is sortable (possible only if the numbers to be swapped have same number of bits set)
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def sameBits(num1, num2):
            num1, num2 = str(bin(num1)), str(bin(num2))
            if num1.count('1') == num2.count('1'):
                return True
            return False
        length = len(nums)
        for i in range(length):
            for j in range(length-1):
                if nums[j] > nums[j+1]:
                    if sameBits((nums[j]), nums[j+1]):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    else:
                        return False
        return True
