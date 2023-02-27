'''
his problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at
the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

--------
0 0 0 0  =====>  4 3 2 1
0 0 0 0          1 1 1 1
-------
'''

def ways2destination(matrix):
    M=len(matrix)
    N=len(matrix[0])

    dp=[[0]*N for _ in range(M)]
    for i in range(M):
        dp[i][N-1]=1
    for j in range(N):
        dp[M-1][j]=1
    for i in range(M-2,-1,-1):
        for j in range(N-2,-1,-1):
            dp[i][j]=dp[i+1][j]+dp[i][j+1]
    #print dp[0][0]

    return dp[0][0]

mat=[[0]*5]*5
print ways2destination(mat)

mat=[[0]*3]*6
print ways2destination(mat)

mat=[[0]*2]*2
print ways2destination(mat)

mat=[[0]*4]*2
print ways2destination(mat)