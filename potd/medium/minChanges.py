# Minimum number of changes to make string beautiful

class Solution:
    def minChanges(self, string: str) -> int:
        changes = 0; length = len(string) // 2
        for block in range(length):
            word = string[block*2: (block+1)*2]
            if word != '00' and word != '11':
                changes += 1
        return changes

s1 = Solution()

res = s1.minChanges(string)

print(res)