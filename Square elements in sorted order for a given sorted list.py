'''
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''

def squarelist(arr):
    if arr[0]>=0:
        for i in range(len(arr)):
            arr[i]=arr[i]**2
        return arr

    res=[]
    lo,hi = 0, len(arr)-1
    while lo<=hi:
        if abs(arr[lo])>abs(arr[hi]):
            res.append(arr[lo]**2)
            lo+=1
        else:
            res.append(arr[hi]**2)
            hi-=1
    return res[::-1]#memory this reverse format'::-1'

def squarelist2(arr):
    lo, hi = 0, len(arr)-1
    i= len(arr)-1
    left = arr[lo]
    right = arr[hi]
    res=[None]*len(arr)
    while lo <= hi:
        if abs(left) > abs(right):
            res[i] = left**2
            lo +=1
            if lo<=len(arr)-1:
                left = arr[lo]
        else:
            res[i] = right**2
            hi-=1
            if hi>=0:
                right = arr[hi]
        i-=1

    return res

arr=[-9, -2, 0, 2, 3]
print "1:", squarelist(arr)
arr=[-9, -2, 0, 2, 3]
print squarelist2(arr)

#exit(0)
arr=[-20, -10, -9, -2, -1]
print "2:", squarelist(arr)
arr=[-20, -10, -9, -2, -1]
print squarelist2(arr)

arr=[5,7,10,20,21]
print "3:", squarelist(arr)
arr=[5,7,10,20,21]
print squarelist2(arr)


arr=[-1,0, 5,7,10,20,21]
print "4:", squarelist(arr)
arr=[-1,0, 5,7,10,20,21]
print squarelist2(arr)