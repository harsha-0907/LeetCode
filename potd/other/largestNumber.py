# This solution is not my own. I have taken this approach from Solutions Tab

def largetNumber(nums):
    # It is clear that the only way to do this is by sorting (customization)
    # Here the only way to rearrange is to check every 2 consecutive strings and swap the strings according comparison operator
    def compare(x, y):
        if x + y > y + x:
            return 1
        elif x + y < y + x:
            return -1
        else:
            return 0
        
    nums[:] = list(map(str, nums))
    nums.sort(key=compare(nums), reverse=True)

    return ''.join nums