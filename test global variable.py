class mycls(object):

    def method1(self, grid):
        M=len(grid)
        N=len(grid[0])
        self.flag=True
        shift=[[-1,0],[1,0],[0,-1],[0,1]]

        def valid(x,y):
            return x>=0 and x<M and y>=0 and y<N

        def method2(grid, i,j):
            #print ("i+j=", i+j)
            if i+j>3:
                self.flag=False
            grid[i][j]=2
            for dx, dy in shift:
                if valid(dx+i, dy+j) and grid[dx+i][dy+j]==0:
                    method2(grid, dx+i, dy+j)

        cnt=0
        for i in range(M):
            for j in range(N):
                if grid[i][j]==0:
                    cnt+=1
                    method2(grid,i,j)
                    print ("flag= ", self.flag)
        return cnt
grid=[[1,1,1,1],[0,0,1,0],[1,0,1,1],[1,1,1,1]]

c=mycls()

print (c.method1(grid))

exit(0)

def mystr(s):
    ans=[]

    def helper(s):
        for ch in s:
            ans.append(ch)
        print ("inside helper func: ", ans, "\n")
    helper(s)
    return ans

def split(s):
    res= s.split("*")
    res=map(int, res)
    print ("res=", res)
    return res
s="abcd123"
res=mystr(s)
print ("result:  ", res)

ss="10*3*5*12"
print (split(ss))