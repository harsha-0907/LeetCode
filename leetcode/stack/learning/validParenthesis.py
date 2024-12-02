# Check if the string is valid

# Here it was more like brute-force which can definately be improved :/
def validParenthesis(expression):
    stack = []
    for ch in expression:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if stack != [] and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif ch == ']':
            if stack != [] and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif ch == '}':
            if stack != [] and stack[-1] == '{':
                stack.pop()
            else:
                return False
        
    if stack == []:
        return True
    return False


# This code makes the code look nice and clean
def validateParenthesis(expression):
    """ Using Dictionary was a better approach and it makes sense"""
    lst=[]
    d= {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in d:
            if len(lst)!=0 and lst[-1]==d[i]:
                lst.pop()
            else:
                return False
        else:
            lst.append(i)
    return True if not lst else False
s = "([])"

res = validParenthesis(s)

print(res)
            