# Check two strings are isomorphic are not

def isomoprhicString(str1,str2):
    
    if len(str1) != len(str2):
        return False
    dict_str1 = {}
    dict_str2 = {}
    
    for i, value in enumerate(str1):
        #print(dict_str1.get(value, []) + [i])
        dict_str1[value] = dict_str1.get(value, []) + [i]
    print(dict_str1.values())
            
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]
    print(sorted(dict_str1.values()))
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False
    
s="abccdb"
t = "xyzzry"
print(isomoprhicString(s,t))