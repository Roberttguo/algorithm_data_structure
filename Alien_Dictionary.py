'''
Leetcode 269 Hard
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

'''


#accepted 3/1/2022
from collections import deque


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        N = len(words)
        # if N==1:
        #    return words[0]#?why have to be commented out? ['aba'] test case expecetd 'ab' instead of 'aba'
        graph = {}
        for w in words:
            for c in w:
                if c not in graph:
                    graph[c] = set()

        indegree = [0] * 26  # words[i] consists of only lowercase English letters.

        # build neighbor graph and indegree
        for i in range(1, N):
            first = words[i - 1]
            second = words[i]
            len1, len2 = len(first), len(second)
            for j in range(min(len1, len2)):
                c1 = first[j]
                c2 = second[j]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[ord(c2) - ord('a')] += 1
                    break  # must break here, remaining char comaparison should be done in next pair
            else:
                if len1 > len2:
                    return ""
        # BFS with topsort
        Q = deque()
        for x in graph:
            if indegree[ord(x) - ord('a')] == 0:
                Q.append(x)
        if len(Q) == 0:
            return ""
        ans = ""

        while len(Q) > 0:
            tmp = Q.popleft()
            ans += tmp
            for nbr in graph[tmp]:
                indegree[ord(nbr) - ord('a')] -= 1
                if indegree[ord(nbr) - ord('a')] == 0:
                    Q.append(nbr)
        return ans if len(ans) == len(graph) else ""