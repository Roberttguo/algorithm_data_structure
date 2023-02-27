'''
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''

def longestDistinctSubarray(arr):

    max_len=0
    mem={}
    start_ind=0 #start index where a sub array contians distinct elements only
    for i in range(len(arr)):
        if arr[i] in mem:
            start_ind = max(start_ind,mem[arr[i]]+1)
        mem[arr[i]]=i
        max_len=max(max_len, i-start_ind+1)
    return max_len

def longestDistinctSubarray_(arr):

    max_len=0
    mem=set()
    start_ind=0 #start index where a sub array contians distinct elements only
    exce_count=0
    for i in range(len(arr)):
        exce_count+=1
        while arr[i] in mem:# remove all elements before current duplicate one
            mem.remove(arr[start_ind])
            start_ind+=1
            exce_count+=1
        mem.add(arr[i])
        max_len=max(max_len, i-start_ind+1)
    print "no of operations:", exce_count
    return max_len


arr=[5, 1, 3, 5, 2, 3, 4, 1]

print longestDistinctSubarray(arr)

arr=[7, 1, 3, 5, 2, 10, 4, 1]

print longestDistinctSubarray(arr)

arr=[7, 1, 3, 5, 2, 10, 4, 11]

print longestDistinctSubarray(arr)

arr=[7, 1, 3, 5, 2, 10, 4, 11,8]

print longestDistinctSubarray(arr)
arr=[7, 7, 7, 7, 2, 10, 4, 11,8]

print longestDistinctSubarray(arr)
print "second way: ", longestDistinctSubarray_(arr)
arr=[7, 7, 7, 7, 2, 10, 4, 11,8,8,8]

print longestDistinctSubarray(arr)

print longestDistinctSubarray_(arr)