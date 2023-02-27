'''
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

def largestProduct(arr):
    arr.sort()
    N = len(arr)
    if arr[N-1]<0:
        return arr[N-1]*arr[N-2]*arr[N-3]
    return max(arr[N-1]*arr[N-2]*arr[N-3], arr[N-1]*arr[0]*arr[1])

arr=[-10,-10,5,2]
print largestProduct(arr)

arr=[-10,-10,5,2,100]
print largestProduct(arr)

arr=[-500, -10,-10,251234,2,100]
print largestProduct(arr)

arr=[-500, 1,0,7,25,2,10]
print largestProduct(arr)