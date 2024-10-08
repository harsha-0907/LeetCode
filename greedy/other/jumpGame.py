# To calculate the minimum number of jumps required to travel from index '0' to 'n'

def minJump(nums):
    pos = 0;n = len(nums)
    while pos < n:
        maxi = 0
        if pos + nums[pos] >= n-1:
            return True
        for j in range(pos+1, pos+nums[pos]+1):
            if j + nums[j] > maxi + nums[maxi]:
                maxi = j
        if pos == maxi or nums[maxi] == 0:
            return False
        else:
            pos = maxi

nums = [3,2,1,0,4]

res = minJump(nums)    

print(res)