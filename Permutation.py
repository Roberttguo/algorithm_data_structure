
ans=[]
def permutation(arr, start):
    if start==len(arr)-1:
        print ("".join(map(str, arr)))
        ans.append("".join(map(str, arr)))
        return
    for i in range(start, len(arr)):
        arr[i], arr[start]=arr[start], arr[i]
        permutation(arr,start+1)
        arr[start], arr[i] =  arr[i], arr[start]


arr=[1,2,3,4]
start=0
permutation(arr,0)
print (ans, len(ans))
