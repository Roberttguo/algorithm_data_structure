'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

'''

#accepted on 3/13/2022, sorting original array is important
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(arr, start, k, tmp=[], tmp2=[], ans=set(), final=[]):
            if k == 0:
                x = "".join(tmp)
                if x not in ans:
                    ans.add(x)
                    final.append(tmp2[:])
                return
            for i in range(start, len(arr)):
                tmp.append(str(arr[i]))
                tmp2.append(arr[i])
                helper(arr, i + 1, k - 1, tmp, tmp2, ans, final)
                tmp.pop()
                tmp2.pop()
            return

        ans = set()
        res = []
        tmp = []
        tmp2 = []
        nums.sort()
        for j in range(0, len(nums) + 1):
            helper(nums, 0, j, tmp, tmp2, ans, res)

        return res