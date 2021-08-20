# Reverse the string while keeping the words in tact in O(1) space

s = ['m','y',' ','n','a','m','e',' ','i','s',' ','j','a','y']

for i in reversed(s):
    temp = []
    i,j=0,0
    while i<len(s):
        while j < len(s) and s[j] == ' ':
            j+=1
        k = j+1
        j=j-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        i = j= k
print(s)