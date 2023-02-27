'''
Write a program to find second minimum and second maximum number from the array
'''

def find_2ndMaxMin(arr):

    max_v=arr[0]
    second_max=arr[0]
    min_v=arr[0]
    second_min=arr[0]

    for e in arr:
        if e>max_v:
            second_max=max_v
            max_v=e
        else:
            if e>second_max:
                second_max=e
        if e<min_v:
            second_min=min_v
            min_v=e
        else:
            if e<second_min:
                second_min=e
    return (min_v, second_min, max_v, second_max)


def find_Positive_2ndMaxMin(arr):

    max_v=-2**32
    second_max=-2**32
    min_v=2**32
    second_min=2**32

    for e in arr:
        if e>=0:
            if e>max_v:
                second_max=max_v
                max_v=e
            else:
                if e>second_max:
                    second_max=e
            if e<min_v:
                second_min=min_v
                min_v=e
            else:
                if e<second_min:
                    second_min=e
    return (min_v, second_min, max_v, second_max)


arr=[0,7,10,-3,-1, 5,7,-20]
print (find_2ndMaxMin(arr))
print (find_Positive_2ndMaxMin(arr))
arr=[2,7,10,-3,-1, 5,7,4,-20]
print (find_2ndMaxMin(arr))
print (find_Positive_2ndMaxMin(arr))
arr=[3, 4, -1, 1]
print (find_2ndMaxMin(arr))
print (find_Positive_2ndMaxMin(arr))
arr=[1,2,0]
print (find_2ndMaxMin(arr))
print (find_Positive_2ndMaxMin(arr))

arr=[1,2,0,1,5,78]
print (find_2ndMaxMin(arr))
print (find_Positive_2ndMaxMin(arr))