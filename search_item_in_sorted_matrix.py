# Given an n*n matrix which is row-wise and column-wise sorted, find the position of target in the matrix
# if it is present in it. Otherwise print "NOT FOUND"

# Ex - 
# [[10, 20, 30, 40],
#  [15, 25, 35, 45],
#  [27, 29, 37, 48],
#  [32, 33, 39, 50]]
# target = 29
# OUTPUT - Found at (2,1)

# In this approach time complexity will be O(n+n) i.e.,linear time.


def searchItemInMatrix(mat, target):
    r,c = 0, len(mat[0])-1
    while r<len(mat) and c>0:
        if mat[r][c] == target:
            return  True
        elif mat[r][c] < target:
            r+=1
        else:
            c-=1
    return False
    


mat = [[10, 20, 30, 40],[15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
target = 23
print(searchItemInMatrix(mat, target))