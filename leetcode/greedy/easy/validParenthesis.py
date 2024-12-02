# To see if the string is a valid string or not
#from collections import deque

def validateParenthesis(string):
    stack = []; pos = 0; length = len(string)
     
    while pos < length:
        ch = string[pos]
        if ch == '(':
            stack.append(ch)
        elif ch == '*':
            stack.append(ch)
        else:
            if '(' in stack:
                last_index = len(stack) - 1 - stack[::-1].index('(')
                del stack[last_index]
            elif '*' in stack:
                last_index = len(stack) - 1 - stack[::-1].index('*')
                del stack[last_index]
            else:
                stack.append(')')
                return False
        pos += 1
    
    # Now we need to bother about the '(' brackets only
    cnt = 0
    for ch in stack:
        if ch == '(':
            cnt += 1
        elif ch == '*' and cnt > 0:
            cnt -= 1
    
    if cnt > 0:
        return False
    return True




string = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

res = validateParenthesis(string)

print(res)