# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
'''
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and
A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and
 (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
'''

def countInversion_bruteforce(arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                count+=1
    return count

import heapq as hq
#heapq, time complexity< O(n^2)?
def countInversion(arr):
    count=0
    hmax=[]
    hmin=[]
    hq.heappush(hmax,-arr[0])
    hq.heappush(hmin, arr[0])
    for i in range(1,len(arr)):
        if arr[i] >hmin[0]:
            hq.heappush(hmax, -arr[i])
            hq.heappush(hmin, arr[i])
        else:
            while hq.heappop(hmin)>arr[i]:
                count+=1
        hq.heappush(h, arr[i])
def countInversion_qsort(arr):
    count = [0]

    def helper(A, start, end, count):
        if start>end:
            return
        mid=(start+end)/2
        pivot=A[mid]
        i,j=start,end
        while i<j:
            while A[i]<pivot:
                i += 1
            while A[j]>pivot:
                j -= 1
            #swap
            A[i], A[j] = A[j], A[i]
            count[0] += 1
            i+=1
            j-=1
        if i<end:
            return helper(A,i, end, count)
        if j>start:
            return helper(A,start,j, count)

    start, end = 0, len(arr)-1
    helper(arr, start, end, count)
    print "after sorting: ",  arr
    return count[0]



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    arr=[2,4,1,3,5]
    print "inversion: ", countInversion_bruteforce(arr)
    print countInversion(arr)

    arr=[5,4,3,2,1]
    print "inversion: ", countInversion_bruteforce(arr)
    print countInversion(arr)

    arr=[2,4,1,6,3,5]
    print "inversion: ", countInversion_bruteforce(arr)
    print countInversion(arr)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
