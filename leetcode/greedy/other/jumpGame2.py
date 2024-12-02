# The solution for the Jump-Game - II

def calculateMinNUmberOfJumps(nums):
    if len(nums) == 1:
        return 0
    jumps = 0; pos = 0; n = len(nums)
    
    while pos < n-1:
        maxi = pos
        for j in range(pos+1, pos+nums[pos]+1):
            if j >= n-1:
                return jumps + 1
            if j + nums[j] > maxi + nums[maxi]:
                maxi = j
        print(maxi)
        pos = maxi; jumps += 1
    
    return -1
        

nums = [2,3,1,1,4]

res = calculateMinNUmberOfJumps(nums)

print(res)