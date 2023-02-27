'''
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that
the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi
respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.



Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true


Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105

'''
#Memorize this approach
#Accepted on 11/6/2021
import heapq
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key=lambda x: x[1])
        minheap=[] #used to store trips based each finish time:(to,from, numPassengers)
        tot=0
        N=len(trips)
        for i in range(N):
            while len(minheap)>0 and trips[i][1] >=minheap[0][0]: #understand here, this mean current does not overlap with that previous earlier fininished trip.
                tot-=minheap[0][2]
                heapq.heappop(minheap)
            tot+=trips[i][0]
            heapq.heappush(minheap, (trips[i][2],trips[i][1],trips[i][0]))
            if tot>capacity: #the position of this line matters in this loop
                return False

        return True