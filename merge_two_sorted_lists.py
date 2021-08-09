
# 2 pointer technique

A = [2,5,6,9,10,15,18]
B = [1,4,5,8,12]

def merge_arrays(A, B):
    a,b = 0,0
    C = []
    while a < len(A) and b < len(B):
        if A[a]>B[b]:
            C.append(B[b])
            b+=1
        else:
            C.append(A[a])
            a+=1
            
    if a<len(A):
        C.extend(A[a:])
    else:
        C.extend(B[b:])    
    
    return C
    
print(merge_arrays(A, B))