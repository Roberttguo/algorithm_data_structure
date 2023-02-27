'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair
(answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

nput: nums = [1,2,3,4]
Output: [1,2,4]
'''

#accepted. Reuse dp based solution for Largest Increasing subsequence
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        if N <= 1:
            return nums
        lis = [1] * N
        nums.sort()
        longest = 1
        # longest_idx=-1

        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    # if longest<lis[i]:
                    #    longest_idx=i
                    longest = max(longest, lis[i])
                    # print "longest=", longest, lis

        ans = []
        prev = -1
        for i in range(N - 1, -1, -1):
            if longest == lis[i] and (prev % nums[
                i] == 0 or prev == -1):  # prev%nums[i]==0 important, eg. lis=[1,2,2,3] correspond to [1,2,3,4], second longest=2<mapping>3, 4%3!=0
                # print "longest=lis[i]", longest, lis[i]
                ans.append(nums[i])
                prev = nums[i]
                longest -= 1
        return ans


