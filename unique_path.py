'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot
 tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at
 any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

#below dfs is timeout. Must use dp way
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [[False] * n for _ in range(m)]
        print (visited)
        shift = [[1, 0], [0, 1]]

        count = [0]

        def dfs(start_x, start_y, m, n, visited, count):
            print ("x= ?", start_x, "y= ?", start_y, "m=?", m, "n= ?", n)
            if start_x == n - 1 and start_y == m - 1:
                count[0] += 1
                print ("count+1:", count[0])
            visited[start_y][start_x] = True
            for x, y in shift:
                if start_y + y < m and start_x + x < n and not visited[start_y + y][start_x + x]:
                    dfs(start_x + x, start_y + y, m, n, visited, count)
            visited[start_y][start_x] = False

        dfs(0, 0, m, n, visited, count)
        return count[0]

#60/63 TCs passed, although it was accepted before as 2/25/2023
class Solution_dp(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*n for _ in range(m)]

        for i in range(n):
            dp[0][i]=1

        for j in range(m):
            dp[j][0]=1

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]



o=Solution()
print (o.uniquePaths(3,7))

o2=Solution_dp()

print (o2.uniquePaths(3,7))
