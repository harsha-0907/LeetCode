class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0; length = len(nums); steps = 1
        while pos < length:
            leap = nums[pos]
            if leap + pos >= length - 1:
                return True
            max_distance = pos + leap; newpos = None
            for posi in range(pos+1, pos+leap+1):
                if posi + nums[posi] > max_distance:
                    newpos = posi
                    max_distance = posi + nums[posi]
            if newpos is None:
                return False
            pos = newpos; steps += 1
        
        return True

                



                