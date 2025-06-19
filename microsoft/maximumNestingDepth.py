

class Solution:
    def maximumNestingDepth(self, string):
        maxDepth = depth = 0
        for ch in string:
            if ch == '(':
                depth += 1
                maxDepth = max(maxDepth, depth)
            elif ch == ')':
                depth -= 1
        
        return maxDepth


obj = Solution()
string = "(1+(2*3)+((8)/4))+1"

print(obj.maximumNestingDepth(string))