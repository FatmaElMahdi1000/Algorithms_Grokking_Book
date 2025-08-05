def evalRPN(tokens):
    stack = []
    
    if len(tokens) > 10000:
        return "Error, len must be less than 10000"
    if tokens[-1] not in ['*', '-','+','/']:
        return "Error: this is not arithmetic expression!"
        
    for token in tokens: 
        if token not in ['*', '-','+','/']:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '*':
                result = a * b
            elif token == '-':
                result = a - b
            elif token == '+':
                result = a * b
            elif token == '/':
                result = int(float(a) / b)
            stack.append(result)
    return stack[0]
        
tokens = ["4","13","5","/","5","+"]
Result = evalRPN(tokens)
print(Result)
