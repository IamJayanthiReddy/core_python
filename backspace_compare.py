# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
# backspace char. Note that after backspace an empty text, the text will continue empty.
# Ex- input - s = 'ab#c', t='ad#c'
# output: true



def backSpaceCompare(s, t):
    stack1 = []
    stack2 = []
    
    for i in s:
        if i!='#':
            stack1.append(i)
        else:
            if stack1:
                stack1.pop()
                
    for i in t:
        if i!='#':
            stack2.append(i)
        else:
            if stack2:
                stack2.pop()
                
    return stack1 == stack2
s= 'ab#c'
t = 'ab#d'
print(backSpaceCompare(s,t))