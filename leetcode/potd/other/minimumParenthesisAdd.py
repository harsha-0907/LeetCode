# The minimum number of parenthesis to added to validate the string

def minimumNumberOfParenthesis(string):
    stack = []; closecnt = 0
    
    for ch in string:
        if ch == '(':
            stack.append('()')
        else:
            if stack == []:
                closecnt += 1
            else:
                stack.pop()
    
    return len(stack) + closecnt

string = "())"

res = minimumNumberOfParenthesis(string)

print(res)