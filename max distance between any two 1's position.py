'''
Given an integer array containg 0 and 1 only, find the max distance between two adjacent 1's
'''


def maxDistance(arr):

    max_dist=0
    N=len(arr)
    first_one, second_one=-1,-1
    first_max, second_max=-1,-1

    for i in range(N):
        if arr[i]==1 and first_one<0: #==second_one:
            first_one=i
            continue
        if arr[i]==1 and first_one>=0:
            second_one=i
            if second_one-first_one>max_dist:
                max_dist=max(max_dist, second_one-first_one)
                first_max=first_one
                second_max=second_one
            first_one=second_one
    print ("first max: ", first_max, "second max: ", second_max, "mid= ", int ((first_max+second_max)/2))
    return max_dist

arr=[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1]

print (maxDistance(arr))

