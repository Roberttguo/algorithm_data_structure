'''
This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes
[3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?
'''

''' 1. Rotating k times----'''
def leftRotateByOne(arr):
    first =arr[0]
    for i in range(1,len(arr)):
        arr[i], arr[i-1]= arr[i-1],arr[i]
    arr[len(arr)-1]=first

def rightRotateByOne(arr):
    last =arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        arr[i], arr[i+1]= arr[i+1],arr[i]
    arr[0]=last

#time complexity is O(k*n)
def rotateKElements(arr, k):
    if not arr or len(arr)==0:
        return arr
    N=len(arr)
    k=k%N
    if k==0:
        return arr
    for j in range(k):
        leftRotateByOne(arr)

    return arr

def rotateKElements_right(arr, k):
    if not arr or len(arr)==0:
        return arr
    N=len(arr)
    k=k%N
    if k==0:
        return arr
    for j in range(k):
        rightRotateByOne(arr)
    return arr

'''---2. Using Auxiliary Array--- this can reduce time complexity'''

def rotateKElements_Auxi(arr, k):
    if not arr or len(arr)==0:
        return arr
    k=k%len(arr)

    auxi_arr=arr[0:k]
    #shift to left
    for i in range(len(arr)-k):
        arr[i]=arr[k+i]
    i=0
    for j in range(len(arr)-k, len(arr),1):
        arr[j]=auxi_arr[i]
        i+=1
    return arr

'''--- 3. By reversing array
We can even solve this problem in O(n) time and O(1) extra space. The idea is to reverse the last k elements of 
the input array and then reverse the remaining n-k elements. Finally, get the right-rotated array 
by reversing the complete array.---'''
#recall rotate = three reverse operation
def reverse(arr, start, end):
    i, j=start,end
    while i<=j:
        arr[i], arr[j]=arr[j], arr[i]
        i+=1
        j-=1
    return arr

def rotateKElements2right_reverse(arr, k):
    if not arr or len(arr)==0:
        return arr
    k=k%len(arr)

    reverse(arr, len(arr)-1-k, len(arr)-1)
    print "first reverse: ", arr
    reverse(arr, 0, len(arr)-2-k)
    print "second reverse: ", arr
    reverse(arr,0, len(arr)-1)

    return arr



arr=[1,2,3,4,5]
print rotateKElements(arr,2)
arr=[1,2,3,4,5]
print rotateKElements_right(arr,2)
arr=[1,2,3,4,5]
print "auxiliary array:", rotateKElements_Auxi(arr, 2)


arr=[1,2,3,4,5]
print rotateKElements(arr,3)
arr=[1,2,3,4,5]
print rotateKElements_right(arr,3)
arr=[1,2,3,4,5]
print "auxiliary array:", rotateKElements_Auxi(arr, 3)

arr=[1,2,3,4,5,6]
print rotateKElements(arr,3)

arr=[1,2,3,4,5,6]
print rotateKElements_right(arr,3)

arr=[1,2,3,4,5,6]
print "auxiliary array:", rotateKElements_Auxi(arr, 3)
arr=[1,2,3,4,5,6,7]
print rotateKElements2right_reverse(arr, 3)