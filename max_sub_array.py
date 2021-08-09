# Given an array of integers of size 'n'. Calculate the max sum of 'k' consecutive elements in the array.
# Example - arr = [1,4,2,10,23,3,1,0,20] and k=4
# Output - 39

# This is solved using sliding window technique instead of using brute force by which time complexity will be O(n*n)


def maxSum(arr, k):
    max_sum = 0
    if len(arr) < k:
        print('Max sum calculation not possible')
        return
    
    n = len(arr)
    window_sum = sum(arr[:k])
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [2,5,1,7,8,2,5,6]
k = 3
print(maxSum(arr, k))