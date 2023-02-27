'''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.



Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109

'''

#Accepted on 1/1/2022
from collections import deque


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        timecomplexity=0
        l, r = 0, 0
        max_len = 0
        min_q = deque()  # used to store min's index within sliding window l>r
        max_q = deque()  # used to store max's index within sliding window l>r
        while l < len(nums) and r < len(nums):
            timecomplexity+=1
            while min_q and nums[min_q[-1]] > nums[r]:
                min_q.pop()
                timecomplexity += 1
            min_q.append(r)

            while max_q and nums[max_q[-1]] < nums[r]:
                max_q.pop()
                timecomplexity += 1
            max_q.append(r)

            #first elements in both min_q and max_q are always minimum and maximum for current sliding window
            if nums[max_q[0]] - nums[min_q[0]] <= limit:
                max_len = max(max_len, r - l + 1)
            else:
                if l == min_q[0]:
                    min_q.popleft()
                if l == max_q[0]:
                    max_q.popleft()
                l += 1
            r += 1
        print ("timecomplexity= ", timecomplexity)
        return max_len
o=Solution()
nums=[8,2,4,7]
limit=4
print (o.longestSubarray(nums,limit))

nums=[1,1,1,1,1,1,1,1,1,1]
limit=1
print (o.longestSubarray(nums,limit))

nums=[1,2,3,4,1,2,3,1,1,1]
limit=1
print (o.longestSubarray(nums,limit))