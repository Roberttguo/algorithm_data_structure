'''

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
'''

#accepted on 2/9/2022 by leetcode
class CustStr(object):

    def __init__(self,x):
        self.x=x

    def __gt__(self, other):
        return self.x+other.x>other.x+self.x

    def __lt__(self, other):
        return self.x + other.x < other.x + self.x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        st = [CustStr(str(x)) for x in nums]
        st.sort()
        st = st[::-1]
        st = [e.x for e in st]

        i = 0
        while st[0] == '0' and i < len(st) - 1:
            i += 1
        st = st[i:]
        return "".join(st)


nums=[3,30,34,5,9]

'''
s=[CustStr('3'), CustStr('30'), CustStr('9'), CustStr('301'), CustStr('5')]

for i in range(len(s)):
    print (s[i].x)
s.sort()
print ("after sort:")
for i in range(len(s)):
    print (s[i].x)
print ("after reverse:")
s=s[::-1]
for i in range(len(s)):
    print (s[i].x)
'''

o=Solution()
print ("answer: ", o.largestNumber(nums))
nums=[3,30,34,5,9, 121,501]

nums=[0,0,0,0,0, 1,0]

print ("answer: ", o.largestNumber(nums))

nums=[0,0,0,0,0, 0,0]

print ("answer: ", o.largestNumber(nums))