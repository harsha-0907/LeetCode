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

    # Optimal
    def canSortArrayOptimal(self, nums: List[int]) -> bool:
        pmax = cmin = cmax = pcnt = 0
        for v in nums:
            ccnt = v.bit_count()
            if pcnt == ccnt:
                cmin = min(cmin, v)
                cmax = max(cmax, v)
            elif cmin < pmax:
                return False
            else:
                pmax = cmax
                cmin = cmax = v
                pcnt = ccnt
        return cmin >= pmax