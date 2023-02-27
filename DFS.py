def maxSum(mat):
    M=len(mat)
    N=len(mat[0])
    sofar=[0]
    max_sum=[0]
    visited=[[False]*N for _ in range(M)]

    def helper(mat, x,y, M,N, visited, sofarsum, max_sum):
        if x==M-1 and y==N-1:
            sofarsum[0] += mat[x][y]
            max_sum[0]=max(max_sum[0], sofarsum[0])
            return
        if x>=0 and x<M and y>=0 and y<N and not visited[x][y]:
            sofarsum[0]+=mat[x][y]
            visited[x][y]=True
            if x+1<M:
                helper(mat, x+1,y, M,N, visited, sofarsum, max_sum)
                sofarsum[0] -= mat[x+1][y]
                visited[x+1][y] = False
            if y+1<N:
                helper(mat, x, y+1, M, N, visited, sofarsum, max_sum)
                sofarsum[0] -= mat[x][y+1]
                visited[x][y+1]=False
    helper(mat,0,0,M, N,visited, sofar,max_sum)
    return max_sum[0]

mat=[[0, 3, 1, 1],
[12, 10, 7, 4],
[1, 5, 5, 1]]

print maxSum(mat)