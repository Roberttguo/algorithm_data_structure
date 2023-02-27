'''
This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements,
return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
'''

def find_fixedpoint(arr):

    l,r = 0,len(arr)-1
    while l<=r:#need to check l==r
        mid=int((l+r)/2)
        if arr[mid]==mid:
            return arr[mid]
        if arr[mid]<mid:
            l=mid+1
        else: #arr[mid]>mid
            r=mid-1
    #print l,r
    #if l==r and arr[l]==l:
    #    return arr[l]
    return False

arr=[-6,0,2,40,60]

print (find_fixedpoint(arr))

arr=[1, 5, 7, 8,10,21]
print (find_fixedpoint(arr))

arr=[0, 5, 7, 8,9,10,21,30,50]
print (find_fixedpoint(arr))