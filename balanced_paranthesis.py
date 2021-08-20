# Valid parenthesis problem

def balancedParanthesis(s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            stack.pop()
    if stack:
        return False
    else:
        return True


s = "({{[{]}})"    
print(balancedParanthesis(s))