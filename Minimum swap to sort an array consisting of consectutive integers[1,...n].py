'''
You are given unsorted array consisting of consecutive integers [1,2,3,...n] without any duplicates. You are allowed to
swap any two elements. Find the minimum numbers of swaps to sort the array in ascending order.
For example, givein the array =[7,1,3,2,5,4,6]
'''

def minSwaps(arr):

    # per property described above, after sorting, each element should be located at index-1,
    # start from index 0, always swap current element with one that current element is supposed to be if current element is not at its supposed location
    # otherwise, just increment index i
    i=0
    swaps=0
    exce_count=0
    while i<len(arr):
        exce_count+=1
        if arr[i]==i+1:
            i+=1
        else:
            swap_index = arr[i]-1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swaps+=1
    print arr, exce_count
    return swaps

arr=[7,1,3,2,5,4,6]

print minSwaps(arr)

arr=[7,1,3,2,4,5,6]

print minSwaps(arr)

arr=[7,1,3,9, 2,4,10,5,8,6]

print minSwaps(arr)

arr=[7,6,5,4,3,2,1]

print minSwaps(arr)