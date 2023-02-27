'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.



Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]


Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
'''

#accepted
#time complexity m*n*k, m=length of words1, n=num of different/unique chars contained in words2, k =maximum count a char time in a given word from words1

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """

        def setMem(w):  # memorize max char count in all words in words2
            m = {}
            for x in w:
                for y in x:
                    if y not in m:
                        m[y] = 1
                    else:
                        m[y] = max(m[y], x.count(y))
            return m

        candidates = []
        mem = setMem(words2)
        for w1 in words1:
            flag = True

            for x in mem:
                if w1.count(x) < mem[x]:
                    flag = False
                    break
            if flag:
                candidates.append(w1)
        return candidates