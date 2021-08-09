



def duplicateZeros(arr):
    stack = []
    for i in arr:
        # if i != 0:
        #     stack.append(i)
        # if i == 0:
        #     stack.append(0)
        #     stack.append(0)
            
        stack.append(i)
        if i == 0:
            stack.append(0)
            
            
    #return stack[:len(arr)]
    #If at all we want to modify arr, then we can use below code.
    for i in range(len(arr)):
        arr[i] = stack[i]
    return arr
            
print(duplicateZeros(arr=[1,0,3,0,5]))