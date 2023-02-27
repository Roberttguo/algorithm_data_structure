'''
1353. Maximum Number of Events That Can Be Attended
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.



Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4


Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
'''

#accepted on 12/24/2021

import heapq as Q


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        N = len(events)
        events.sort()
        count = 0
        max_end = 0
        for i in range(N):
            max_end = max(max_end, events[i][1])

        # iterate every day from start day till max_end day to check a possible attending event
        day = events[0][0]
        hq = []
        idx = 0  # event iteration index
        while day <= max_end:
            while len(hq) > 0 and hq[0] < day:#if event end day is less than current possible attend day, skip it
                Q.heappop(hq)

            while idx < N and events[idx][0] == day:
                Q.heappush(hq, events[idx][1])  # add all events' end day to heap q when they have  the same start day
                idx += 1
            if len(hq) > 0:
                count += 1
                Q.heappop(hq)

            day += 1
        return count

events= [[1,2],[2,3],[3,4],[1,2]]

o=Solution()
print (o.maxEvents(events))