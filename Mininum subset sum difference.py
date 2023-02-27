'''
Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the
subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is
the smallest possible difference.
'''

#Knapck way(recurssion) with memorization
i=0
def knapSack(tot_sum, sofar_sum, s1, arr, n, mem):
    global i
    if n==0: # or sofar_sum>tot_sum/2:
        print ("i: ", i)
        i+=1
        return abs(tot_sum-2*sofar_sum)

    if (n, sofar_sum) in mem:
        return mem[(n, sofar_sum)]
    #case1 include arr[n-1]
    #s1.add(n-1)
    x1=knapSack(tot_sum, sofar_sum + arr[n - 1], s1, arr, n-1, mem)
    #case2 exclude arr[n-1]
    x2=knapSack(tot_sum, sofar_sum, s1, arr, n-1, mem)
    mem[(n,sofar_sum)]=min(x1,x2)
    return mem[(n,sofar_sum)]

arr=[5,10,15,20,25]
n=len(arr)
s1=set()
tot=sum(arr)
mem={}
print (knapSack(tot,0, s1,arr,n, mem), s1)
