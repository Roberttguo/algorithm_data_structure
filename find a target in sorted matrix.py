
def searchMatrix( matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    M=len( matrix)
    N=len ( matrix[0])

    l,r=0, N- 1
    t,b=0,M - 1
    while l<=r and t<=b:
        mid_h=int((r+l ) /2)
        mid_v=int((t+b ) /2)
        print ("mid_h= ", mid_h)
        print("mid_v= ", mid_v)
        if matrix[mid_v][mid_h]==target:
            return True
        else:
            if target<matrix[mid_v][mid_h]:
                r=mid_h
                b=mid_v
            else:
                l=mid_h +1
                t=mid_v +1
        if mid_h==N-1 and mid_v==M-1 or mid_h==0 and mid_v==0:
            break
    return False

matrix=[[-5]]
target=-5
print (searchMatrix( matrix, target))
matrix=[[1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]]
target=20
print (searchMatrix( matrix, target))

print ("Diagonals:")
for i in range(len(matrix)):
    for j in range(i, len(matrix[0])):
        print(matrix[i][j], matrix[j][i])