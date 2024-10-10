# To find the maximum width of the ramp 


def findMaxWidthBad(nums):
    """This is highly un-optimized, solve it using montonic stack"""
    # The ramp has a width 
    # M-1
    # First, we will index each number in a dictionary., the first occurence and the last occurence
    # We only need first/last as the largest width can be obtained from first & last occurences only
    
    dict1 = dict(); length = len(nums)
    
    for pos in range(length):
        num = nums[pos]
        if num in dict1:
            # The number already exists
            # So, we need to modify the first and last places
            dict1[num][1] = pos
        else:
            dict1[num] = [pos,pos]
    nums = sorted(dict1.keys()); length = len(nums)
    
    # for i in nums:
    #     print(i, dict1[i], end=' ')
    start = [dict1[i][0] for i in nums]
    end = [dict1[i][1] for i in nums]
    #print(dict1)
    #print(end)
    def getMax(pos):
        maxpos = 0
        for i in range(pos, length):
            if end[i] > maxpos:
                maxpos = end[i]
                maxele = nums[i]
        
        return maxele, maxpos
    
    maxele, maxpos = getMax(0); maxwidth = 0
    #print(maxele, maxpos)
    
    for pos in range(length):
        ele = nums[pos]; st_index = start[pos]; ed_index = end[pos]
        if ele > maxele:
            maxele, maxpos = getMax(pos)
            #print(maxele, maxpos, pos)
            maxwidth = max(maxpos - st_index, maxwidth)
            
        else:
            maxwidth = max(maxwidth, maxpos-st_index)
        
    return maxwidth

def findMaxWidthUsingStack(nums):
    """ We will be using Monotonic Stack to solve this question"""
    stack = []
    max_width = 0
    # Traverse the list to construct the stack with indices of elements in increasing order
    for i in range(len(nums)):
        if not stack or nums[stack[-1]] > nums[i]:
            stack.append(i)

    # Traverse the list again from right to left to find the maximum ramp width
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            max_width = max(max_width, i - stack.pop())

    return max_width


nums = [9,8,1,0,1,9,4,0,4,1]

res = findMaxWidthUsingStack(nums)

print(res)