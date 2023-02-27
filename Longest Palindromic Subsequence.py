'''
516. Longest Palindromic Subsequence
Medium

3942

229

Add to List

Share
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing
the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

#accepted by leetcode. Due to 1 <= s.length <= 1000, brute force does not work, dp way works and it is only option.
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if s == s[::-1]:
            return N
        # max_len=0
        '''brute force way, got TLE due to 1<<N'''
        '''
        for mask in range(1,1<<N):
            subseq=""
            for i in range(N):
                if (1<<i)& mask:
                    subseq+=s[i]
            if subseq==subseq[::-1]:# is palindrome
                max_len=max(max_len, len(subseq))
        '''

        # dp=[[0]*N for _ in range(N)]

        def helper(s, start, end, mem):
            res = None
            if start > end:
                return 0
            if start == end:
                return 1
            if (start, end) in mem:
                return mem[(start, end)]

            if s[start] == s[end]:
                res = 2 + helper(s, start + 1, end - 1, mem)
            else:
                res = max(helper(s, start + 1, end, mem), helper(s, start, end - 1, mem))
            mem[(start, end)] = res

            return mem[(start, end)]

        mem = {}
        return helper(s, 0, len(s) - 1, mem)

