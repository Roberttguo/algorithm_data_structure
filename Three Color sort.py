# sort a color list in R, G, B order, for example, ['G','B', 'G','B','R','R']  ==>> ['R',R', 'G', 'G', 'B','B']

def sortColor(arr):

    N=len(arr)
    i,k,j=0,0, N-1# those indexes correspond to R, G, B
    while k<=j:
        if arr[k]=='R':
            arr[k], arr[i]=arr[i], arr[k]
            k+=1
            i+=1
        elif arr[k]=='G':
            k+=1
        else: #arr[k]=='B'
            arr[k], arr[j] = arr[j], arr[k]
            j-=1

    return arr

arr=['G','B', 'G','B','R','R']
print sortColor(arr)

arr=['G','B', 'G','B','R','R', 'G', 'G','B']
print sortColor(arr)

arr=['R','B', 'G','B','R','R', 'G', 'G','B']
print sortColor(arr)

arr=['R','R', 'R','R','R','R']#, 'G', 'G','B']
print sortColor(arr)
