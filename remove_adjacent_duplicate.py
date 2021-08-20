# GIven a string S of lowercase letters, you have to perform all duplicate removals. A duplicate removal consists of choosing
# tow adjacent and  equal letters, and removing them.

# input = 'abccdeffeg'
# outpt = 'abdg'

def removeAdjacentDuplicates(s):
    stack = []
    for c in s:
        
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)
            
print(removeAdjacentDuplicates(s="abccdeffege"))