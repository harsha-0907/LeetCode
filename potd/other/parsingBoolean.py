# To parse a boolean expression

def parseBoolean(expression):
    def evaluateExpression(expr, op):
        exp1 = True if expr[0] == 't' else False
        if op == '!':
            return 't' if expr[0] == 'f' else 'f'
        for i in expr[1:]:
            if i == 't':
                exp = True
            else:
                exp = False
            if op == '|':
                exp1 = exp or exp1
            elif op == '&':
                exp1 = exp and exp1
        return 't' if exp1 else 'f'

    stack = []
    for ch in expression:
        if ch == ')':
            expr = ""
            for e in range(len(stack)):
                ele = stack.pop()
                if ele == "!" or ele == "|" or ele == "&":
                    stack.append(evaluateExpression(expr, ele))
                    break
                elif ele == '(':
                    continue
                else:
                    expr += ele
        elif ch == ',':
            continue
        else:
            stack.append(ch)
    
    return True if stack[-1] == 't' else False


expression = "!(&(f,t))"

res = parseBoolean(expression)

print(res)