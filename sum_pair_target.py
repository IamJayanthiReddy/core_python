# 2 pointer technique

def sum_pair(arr, target):
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]+arr[j] == target:
            print(arr[i], arr[j])
            #return
        if arr[i]+arr[j] < target:
            i = i+1
        else:
            j = j-1
    return False


arr = [1,2,4,5,8,9,11,14]
target = 6
res = sum_pair(arr, target)
#print(res)