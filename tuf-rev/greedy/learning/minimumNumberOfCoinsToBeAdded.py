
class Solution:
    def minimumAddedCoins(self, coins:list, target: int) -> int:
        current_max = 0
        additions = 0
        index = 0

        while current_max < target:
            if index < len(nums) and nums[index] <= current_max + 1:
                current_max += nums[index]
                index += 1
            else:
                current_max += current_max + 1
                additions += 1

        return additions

        
obj = Solution()
target = 19
coins = [1,4,10]
result = obj.minimumAddedCoins(coins=coins, target=target)

print(result)

