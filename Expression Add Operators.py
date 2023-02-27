'''
Given a string num that contains only digits and an integer target, return all possibilities to add the binary
operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.



Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''

#Accepted, but solution is from Youtube, need to understand it fully
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []

        def DFS(start, path, sofarEva, preNum, s, target):
            if start == len(s):
                if sofarEva == target:
                    ans.append(path)
                    return

            for i in range(start, len(s)):
                if i > start and s[start] == '0':
                    break
                num = int(s[start:i + 1])
                if start == 0:
                    DFS(i + 1, path + str(num), sofarEva + num, num, s, target)
                else:
                    DFS(i + 1, path + "+" + str(num), sofarEva + num, num, s, target)
                    DFS(i + 1, path + "-" + str(num), sofarEva - num, -num, s, target)
                    DFS(i + 1, path + "*" + str(num), sofarEva - preNum + preNum * num, preNum * num, s, target)# this line import need to check why we have to sofarEva - preNum + preNum * num

        DFS(0, "", 0, 0, num, target)
        return ans

