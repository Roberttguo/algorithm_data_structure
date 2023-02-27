'''

'''
import math

def numberOfWays(arr, k):
    # Write your code here
    count = 0
    mem = {}
    for i in range(len(arr)):
        if arr[i] in mem:
            mem[arr[i]].add(i)
        else:
            mem[arr[i]] = set([i])

    for i in range(len(arr)):
        if k - arr[i] in mem:
            if k!=2*arr[i]:
                t1 = len(mem[k - arr[i]])
                t2= len(mem[arr[i]])
                count+=t1*t2
            else:
                t2 = len(mem[arr[i]])
                c=math.factorial(t2)/(2*math.factorial(t2-2))
                count+=c
            mem.pop(k - arr[i])  # .remove(i)
            if arr[i] in mem:
                mem.pop(arr[i])
            # if len(mem[k-arr[i]])==0:
            #  mem.pop(k-arr[i])
            #count += 1 * t

    return int(count)

arr = [1, 2, 3, 4, 3]
k=6
print ("pairs: ", numberOfWays(arr, k))
arr = [1, 5, 3, 3, 3]
k=6

print ("pairs: ", numberOfWays(arr, k))

arr = [1, 1, 3, 3, 1,1,0,2,2]
k=2

print ("pairs: ", numberOfWays(arr, k))