# To convert a infix to postfix expression

def infixtoPostfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
    postfix_notation = ""
    stack = []

    for ch in expression:
        if ch.isalpha() or ch.isdigit():  # Check if the character is an operand
            postfix_notation += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix_notation += stack.pop()
            stack.pop()  # pop the '(' from the stack
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence[stack[-1]] >= precedence[ch]):
                postfix_notation += stack.pop()
            stack.append(ch)
    while stack:
        postfix_notation += stack.pop()
    
    return postfix_notation


expression = "a+b*(c^d-e)^(f+g*h)-i"
answer = "abcd^e-fgh*+^*+i-"

res = infixtoPostfix(expression)

print(res, res == answer)