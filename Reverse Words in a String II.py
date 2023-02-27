'''
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.



Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]
'''

#accepted on 3/13/2022
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        def reverse(arr, i, j):  # i<=j

            while i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return

        start, end = 0, 0
        n = len(s)
        while end < n:
            while end < n and s[end] != " ":
                end += 1
            reverse(s, start, end - 1)
            start = end + 1
            end += 1
        # print ("rev: ", s)
        reverse(s, 0, n - 1)

