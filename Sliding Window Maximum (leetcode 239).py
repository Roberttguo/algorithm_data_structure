'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
#Accepted on 2/24/2022 two ways-
#(1) deque, <a> check if first element is out of the k sliding window bound, remove it if yes.
# <b> maintain the deque in DSC order when inserting current right element.
# <c> always pick up first element in deque as max and add it to ans[]
#(2) heapq way, similar above

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        if k >= N:
            return [max(nums)]
        if k == 1:
            return nums
        mq = deque()
        i = 0
        ans = []
        while i < k:
            if len(mq) == 0:
                mq.append((nums[i], i))
            else:
                if mq[len(mq) - 1][0] >= nums[
                    i]:  # maintain decsending order so that first element in mq always maximum
                    mq.append((nums[i], i))
                else:
                    while len(mq) > 0 and mq[len(mq) - 1][0] < nums[i]:
                        mq.pop()
                    mq.append((nums[i], i))
            i += 1

        ans.append(mq[0][0])
        # at this point, i=k
        while i < N:
            # check if front element is out of k window size, remove it if yes
            if mq[0][1] < i + 1 - k:
                mq.popleft()
            if len(mq) == 0:
                mq.append((nums[i], i))
            else:
                if mq[len(mq) - 1][0] >= nums[
                    i]:  # maintain decsending order so that first element in mq always maximum
                    mq.append((nums[i], i))
                else:
                    while len(mq) > 0 and mq[len(mq) - 1][0] < nums[i]:
                        mq.pop()
                    mq.append((nums[i], i))
            ans.append(mq[0][0])
            i += 1
        return ans



#following is accepted too.
import heapq


class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        if k == 1:
            return nums
        if k >= N:
            return [max(nums)]
        hq = []
        i = 0
        while i < k:
            heapq.heappush(hq, (-nums[i], i))
            i += 1

        ans = [-hq[0][0]]
        while i < N:
            heapq.heappush(hq, (-nums[i], i))

            while hq[0][1] < i + 1 - k:
                heapq.heappop(hq)

            ans.append(-hq[0][0])
            i += 1
        return ans