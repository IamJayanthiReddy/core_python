# Given an input string, write a function that returns run length encoded string for the input, i.e., does string compression.
# input - wwwwaaadexxxxxxx
# output - w4a3d1e1x6

def consecutiveCountOfString(s):
    
    if len(s)<=1:
        return s
    ans = ''
    count = 1
    for c in range(1, len(s)-1):  
        if s[c] == s[c-1]:
            count+=1
        else:
            ans+=s[c-1]+str(count)
            count = 1
    ans+=s[c]+str(count)
    if len(ans) > len(s):
        return s
    return ans
    
    
s = "wwwwaaadexxxxxxx"
print(consecutiveCountOfString(s))