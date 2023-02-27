
'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''

#Accepted but why this works?
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0

        for x in nums:
            a = (a ^ x) & (~b)
            b = (b ^ x) & (~a)
        return a


    def sumbits(self, a, b):
        s=bin(b)[2:]
        aa=list(a)
        print ("s=",s, "aa=?", aa)
        for i in range(len(s)):
            aa[i]=str(int(aa[i])+int(s[i]))
        return "".join(aa)

    def singleNumber2(self, nums):
        a=bin(nums[0])[2:]
        for i in range(1,len(nums)):
            a=self.sumbits(a, nums[i])
        return a


nums=[2,3,1,3,1,5,1,3,2,2]
o=Solution()

print (o.singleNumber2(nums))
