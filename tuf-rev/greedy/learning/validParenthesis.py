
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == '*':
                stack.append(ch)
            else:
                pos = len(stack) - 1; flag = False
                if pos == -1:
                    return False
                while pos >= 0:
                    if stack[pos] == '(':
                        stack.pop(pos)
                        flag = True
                        break
                    pos -= 1
                
                if not flag:
                    # Considering * -> (
                    stack.pop()

        if stack == []:
            return True
        else:
            for ele in stack:
                if ele == '(':
                    break
            else:
                return True # All *'s only

            newstack = []
            for ele in stack:
                if ele == '(':
                    newstack.append('(')
                else:
                    if newstack == []:
                        continue
                    else:
                        newstack.pop()
            
            if newstack == []:
                return True
            
            return False