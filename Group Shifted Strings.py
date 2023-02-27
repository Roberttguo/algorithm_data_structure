'''

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.



Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]
Output: [["a"]]

'''


#accepted 3/10/2022
from collections import defaultdict

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ans=defaultdict(list)
        #the same shifting sequence means the distance between adjacent characters in given string remains the same,
        # for example, 'abc' and 'xyz' are the same shifting sequence because 'a'->'b'->'c' is 11, 'x'->'y'=>'z' is 11 too.
        for w in strings:
            pat=""
            for i in range(1, len(w)):#all single character belong to the same group?
                pat+=str((ord(w[i])-ord(w[i-1]))%26)
                pat+="#"#why I added this delimiter because ord('l')-ord('a')=11, same as ord('b')-ord('a', ord('c')-ord('b'). Adding '#' or other special char can distinguish them

            ans[pat].append(w)
        return ans.values()

o=Solution()
strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print (o.groupStrings(strings))

strings = ["abc","bcd","acef","xyz","az","ba","a","z","a","b", "p", "Y"] #need to clarify the each single capital letter belongs to the same group as low case lettere?
print (o.groupStrings(strings))