'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.



Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


Constraints:

2 <= n <= 58
'''

#Accepted, recurssion +memorization

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        def product(n, mem): #this method is important
            if n == 1:
                return 1

            if n in mem:
                return mem[n]
            ans = 1 * (n - 1)
            i = 1
            while i < n:
                first = i
                second = (n - i)
                ans = max(ans, first * (max(second, product(second, mem))))#this line is deduced from 4=1+3, 2+2,=> 1*3, 2*2, etc, 5=1+4,2+3, 2+2+1 ...
                i += 1
            mem[n] = ans
            return ans


#dp is fast accepted too.

class Solution2(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        if n == 2:  # 2=1+1
            return 1
        if n == 3:  # 3=1+2, max product=1*2, 3=1+1+1 +product=1
            return 2
        if n == 4:  # 4=1+3, 4=2+2, max product=2*2=4
            return 4

        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            for k in range(i, 0, -1):
                dp[i] = max(dp[i], dp[k] * dp[i - k])

        return dp[n]