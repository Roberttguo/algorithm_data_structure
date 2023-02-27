'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
'''

#accepted 2/27/2022

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)

        sums = [0] * N
        sums[0] = nums[0]
        hash_map = {}
        #purpose is to find all the same reminder of subarrays via prefix sum, when two of them is deducted, reminder is
        # 0, such subarry can be divisble by k apparently. for example, [8,9,7,8,9]
        # 8, presum: [8,17,24,32,41], presum%K: [0,1,0,0,1]
        for i in range(N):
            sums[i] = sums[i - 1] + nums[i]
            #r = (sums[i] % k + k) % k this way also works if there are negative elements
            r = sums[i] % k
            if r in hash_map:
                hash_map[r] += 1
            else:
                hash_map[r] = 1

        # print "hash: ", hash_map
        ans = 0
        for k, v in hash_map.items():
            if k == 0:#if reminder is 0, all subarrys should be included
                ans += v
                # continue
            if v > 1:
                c = v * (v - 1) / 2
                ans += c
        return ans