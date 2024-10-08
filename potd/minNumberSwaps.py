# To find the number of swaps to make the string balanced

import math

def countMinimumNumberOfSwaps(string):
    stack = []; cnt = 0
    for ch in string:
        if ch == '[':
            stack.append('[')
        else:
            if stack != []:
                stack.pop()
            else:
                cnt += 1
    return mth.ceil(cnt/2)
    
string = "[[[]]]][][]][[]]][[["

res = countMinimumNumberOfSwaps(string)

print(res)