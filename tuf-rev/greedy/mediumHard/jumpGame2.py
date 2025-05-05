
class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0; length = len(nums); steps = 1
        while pos < length:
            leap = nums[pos]
            if leap + pos >= length-1:
                return steps
            newpos = pos; max_distance = pos + leap
            for posi in range(pos+1, pos+leap+1):
                if posi + nums[posi] > max_distance:
                    newpos = posi
                    max_distance = posi + nums[posi]
            
            newpos = posi; steps += 1
        
        return steps
