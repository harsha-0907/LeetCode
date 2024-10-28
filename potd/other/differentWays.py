# Different expressions from the evaluating expression

def generateExpressions(expr):
    def addBrackets()
    openbrackets = [0]; closebrackets = [5]
    n = len(expr); number_of_expr = 0
    for i in range(n-1):
        if expr[i] in "*+-":
            openbrackets.append(i)
            closebrackets.append(i+1)
            number_of_expr += 1
    
    print(openbrackets, closebrackets)


expr = "2-1-1"
generateExpressions(expr)