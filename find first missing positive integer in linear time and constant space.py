'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def firstMissingInteger(arr):

    min_v=1
    d={}# this is not constant space
    #following can say O(n) linear time,.
    for e in arr:
        if min_v==e:
            min_v+=1
        else:
            if e>0:
                d[e]=1
    while min_v in d:
        d.pop(min_v)
        min_v+=1
    return min_v

arr=[1, 2, 1, 0]
print firstMissingInteger(arr)
arr=[3, 4, -1, 1]
print firstMissingInteger(arr)
arr=[7, 8, 9, 11, 12]
print firstMissingInteger(arr)
arr=[]
print firstMissingInteger(arr)
arr=[0]
print firstMissingInteger(arr)
arr=[-10, -3, -100, -1000, -239, 1]
print firstMissingInteger(arr)
arr=[1, 1]
print firstMissingInteger(arr)
arr=[1, -1, -5, -3, 3, 4, 2, 8]
print firstMissingInteger(arr)