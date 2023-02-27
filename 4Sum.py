'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

#accepted on 9/2/2021, O(n^3) time complexity
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(nums)
        if N < 4:
            return None
        nums.sort()
        ans = {}
        for i in range(N - 1):
            for j in range(i + 1, N,1):
                two_sum = nums[i] + nums[j]
                l, r = j + 1, N - 1
                while l < r:
                    #print i,j,l,r
                    tot = two_sum + nums[l] + nums[r]
                    if tot < target:
                        l += 1
                    elif tot > target:
                        r -= 1
                    else:  # tot=target
                        ans.setdefault((nums[i], nums[j], nums[l], nums[r]),0)
                        # to avoid duplicate, move forward and backward for l,r
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        #following should not be in front of above two loops.
                        l+=1
                        r-=1

                while j +1< N and nums[j] == nums[j + 1]:
                    j += 1
            while i < N - 1 and nums[i] == nums[i + 1]:
                i += 1
        ans=map(list, ans)
        return ans
nums=[1,0,-1,0,-2,2]
target=0
o=Solution()
print (o.fourSum(nums,target))
nums=[2,2,2,2,2]
target=8
print (o.fourSum(nums,target))

nums=[-1,0,-5,-2,-2,-4,0,1,-2]
target=-9
print (o.fourSum(nums,target))