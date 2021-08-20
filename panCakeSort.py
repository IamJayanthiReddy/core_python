
def flip(arr, k):
    start = 0
    while start <= k-1:
        temp = arr[start]
        arr[start] = arr[k]
        arr[k]=temp
        start+=1
        k-=1
    
def findMax(arr, n):
    mi = 0
    for i in range(n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def panCakeSort(arr, n):
    curr_size = n
    while curr_size > 1:
        mi = findMax(arr, curr_size)
        if mi != curr_size - 1:
            flip(arr, mi)
            flip(arr, curr_size-1)
        curr_size-=1
        
def printArray(arr, n):
    for i in range(0,n):
        print ("%d"%( arr[i]),end=" ")
       
arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
panCakeSort(arr, n);
print ("Sorted Array ")
printArray(arr,n)
# k = 3
# f = flip(arr, k)
#print(f)