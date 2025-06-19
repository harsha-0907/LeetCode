
class Solution:
    def removeOutermostParenthesis(self, arr):
        stackCount = 0; newStr = ""
        for ch in arr:
            if ch == '(':
                stackCount += 1
                if stackCount != 1:
                    newStr += '('
            elif ch == ')':
                stackCount -= 1
                if stackCount != 0:
                    newStr += ')'
        return newStr

obj = Solution()
arr = "(()())(())"

print(obj.removeOutermostParenthesis(arr))
            