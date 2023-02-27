'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

#accepted on 11/2/2021
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        shift =[[0 ,1], [0 ,-1] ,[1 ,0], [-1 ,0]]
        M, N= len(board), len(board[0])

        def validpos(x, y):
            return x >= 0 and x < M and y >= 0 and y < N

        def DFS(board, i, j, word, level):
            if level == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j > len(board[0]) or level >= len(word):
                return False
            ans = False
            ori = board[i][j]
            board[i][j] = '*'
            for dx, dy in shift:
                if validpos(dx + i, dy + j) and board[i + dx][j + dy] == word[level]:
                    ans |= DFS(board, i + dx, j + dy, word, level + 1)

            board[i][j] = ori
            return ans

        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                level = 0
                if board[i][j] == word[level]:
                    res |= DFS(board, i, j, word, level + 1)

        return res