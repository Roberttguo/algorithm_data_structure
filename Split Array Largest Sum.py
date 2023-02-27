'''
Leet code 410 Hard;

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
'''

'''
This question is really similar to 1231. Divide Chocolate.

Here, you want to minimize the largest sum among m subarrays. However, you can also think the other way round: as I move from left to right, and I cut off a subarray the moment before its sum exceed a certain number (such that the subarray sum is kept <= that number), do I get m subarrays, or less? And how small can that number be? Because if you think about it, the lower that number is, the more subarrays I will have.

So this is now formulated into a search-and-decision problem.

For search, you can use binary search. Because let's say, you come up with a big number, and the array can be 
split into <= m subarrays, with the subarray sum <= that big number. Then any bigger number will also definitely work. 
Yet, the minimum number to satisfy this condition may still be <= that big number you came up with. So by using binary 
search, you cut the search portion into O(log(sum(nums))) time.

So why are the starting and ending point of the binary search max(nums) and sum(nums) respectively?

Because every subarray needs any least one number, and when you have a number that couldn't fit into a subarray by 
itself, you end up with a subarray that 'burst', that's why you have to make sure that even the largest of nums also 
can fit into a subarray by itself.

Another thing to note is that 1 <= m , and when m = 1, your entire array is as subarray by itself, so the upper limit 
should be the sum of the array.

As for the work() function, it goes through the nums from left to right and see that given i (upper limit on subarray sum), can we split the array into m or less subarrays? This has a time complexity of O(n).

Together, you get runtime of O(n*log(sum(nums)))

Code with explanation:
'''

#Accepted on 2/17/2022
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        N = len(nums)
        tot = sum(nums)
        max_v = max(nums)
        if m == 1:
            return tot
        if m == N:
            return max_v

        def howManySplit(mid):
            sofar = 0
            req_grp = 1 #pay attention here, initialzie as 1 instead of 0 here
            for i in range(N):
                sofar += nums[i]
                if sofar > mid:
                    req_grp += 1
                    sofar = nums[i]  # reset sofar sum to current element nums[i] to recalculate
            return req_grp <= m

        l, r = max_v, tot + 1
        while l < r:
            mid = (l + r) / 2

            if howManySplit(mid):  # required split groups <given split groups m, so mid to go smaller
                r = mid  # increase next mid
            else:  # bigger than m, each group need to contains more elements, mid goes bigger
                l = mid + 1
        return r
