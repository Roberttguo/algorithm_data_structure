'''
Leetcode 247

Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]
'''

#Accepted on 3/14/2022

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        def helper(cur, remain, res=[]):
            if remain == 0:
                res.append(cur)
                return

            for k, v in map.items():
                # 0 cannot be in leading pos, when k==2, unable to add '0' to current 'cur'
                if remain == 2 and k == '0':
                    continue
                helper(k + cur + v, remain - 2, res)

        res = []
        if n % 2 != 0:  # odd fill both sides for given middle char '0','1' and '8'
            helper("0", n - 1, res)
            helper("1", n - 1, res)
            helper("8", n - 1, res)
        else:
            helper("", n, res)

        return res
