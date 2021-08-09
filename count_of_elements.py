# Given two sorted lists A and B, create a separate list C such that
# C[i] = count of number of elements in A is lesser than B[i]
# Example - A = [1,2,4,7,9], B = [9,19,14,15,18]
# OUTPUT - C = [4,5,5,5,5]

# 2 pointer technique

A = [1,2,4,7,9]
B = [9,19,14,15,18]

def findCountInA(A, B):
    a=0
    C= []
    for b in range(len(B)):
        count = 0
        while a < len(A) and A[a] < B[b]:
            count+=1
            a+=1
        if not C:
            C.append(count)
        else:
            C.append(count+C[-1])
    return C

print(findCountInA(A, B))