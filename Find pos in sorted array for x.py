

def findPos(arr, x):

    l,r=0,len(arr)-1
    if x<arr[l]:
        return 0
    if x>arr[r]:
        return r+1
    while l<=r:
        mid=int((l+r)/2)
        if arr[mid]==x:
            k=mid
            while k>0 and arr[k]==x:
                #if arr[k]==x:
                k-=1
            return k
        else:
            if arr[mid]>x:
                r=mid-1
            else:#arr[mid<x
                l=mid+1
    return r+1
    ''''''
    if arr[mid]<x:
        while mid>0 and arr[mid]<x:
            mid-=1
        return mid
    else:
        return mid+1
    ''''''

arr=[3,5,6,11]
x=7

print (findPos(arr,x))

#exit()
arr=[3,5,9,13]
x=2

print (findPos(arr,x))
arr=[3,5,9,13]
x=15

print (findPos(arr,x))

arr=[3,5,9,13, 13, 13]
x=15

print (findPos(arr,x))

arr=[3,5,9,13, 13, 13]
x=13

print (findPos(arr,x))
