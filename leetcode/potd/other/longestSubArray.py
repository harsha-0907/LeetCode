# The longest sub-array with maximum bitwise AND

def longestSubArray(nums):
    max_sum = max(nums)
    max_len = 0
    curr_len = 0

    for i in range(len(nums) - 1):
        and_result = nums[i] & nums[i + 1]
        if and_result == max_sum:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0

    return max_len + 1  # Add 1 for the last element

nums = [96317,96317,96317,96317,96317,96317,96317,96317,96317,279979]
print(longestSubArray(nums))