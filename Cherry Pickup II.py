'''
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.

'''

#Accepted 3/20/2022 my own method

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        shift = [[1, -1], [1, 0], [1, 1]]
        self.runtime=0
        def validPos(x, y):
            return x >= 0 and x < M and y >= 0 and y < N

        def helper(grid, x1, y1, x2, y2, mem):
            self.runtime+=1
            if x1 == len(grid) - 1 or x2 == len(grid) - 1: #either robot reaches the bottom row in grid
                if y1 != y2:
                    return grid[x1][y1] + grid[x2][y2]
                else:
                    return grid[x1][y1]

            if (x1, y1, x2, y2) in mem:
                return mem[(x1, y1, x2, y2)]
            tot = 0
            if x1 == x2 and y1 == y2:  # both robots meet at the same cell
                tot += grid[x1][y1]
            else:
                tot += grid[x1][y1] + grid[x2][y2]
            local_max = 0
            for dx1, dy1 in shift:
                for dx2, dy2 in shift:
                    if validPos(x1 + dx1, y1 + dy1) and validPos(x2 + dx2, y2 + dy2):
                        subt = helper(grid, x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2, mem)
                        local_max = max(local_max, subt)

            tot += local_max
            mem[(x1, y1, x2, y2)] = tot
            return mem[(x1, y1, x2, y2)]

        mem = {}
        return helper(grid, 0, 0, 0, N - 1, mem), self.runtime


grid=[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
o=Solution()
print (o.cherryPickup(grid))