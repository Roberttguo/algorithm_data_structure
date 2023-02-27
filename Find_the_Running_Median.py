'''

The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
Example
a=[7,3,5,2]
Sorted          Median
[7]             7.0
[3, 7]          5.0
[3, 5, 7]       5.0
[2, 3, 5, 7]    4.0
'''
import heapq as q


#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
#accepted by Hackrank
def addToHeap(num, min_heap, max_heap):
    if not min_heap or num<-min_heap[0]:
        q.heappush(min_heap, -num)
    else:
        q.heappush(max_heap, num)


def rebalanceHeap(min_heap, max_heap):
    if len(min_heap) >= len(max_heap) + 2:
        x = q.heappop(min_heap)
        q.heappush(max_heap, -x)
    if len(min_heap) + 2 <= len(max_heap):
        x = q.heappop(max_heap)
        q.heappush(min_heap, -x)


def getMedian(min_heap, max_heap):
    if len(min_heap) == len(max_heap):
        return float((-min_heap[0] + max_heap[0]) / 2.0)
    else:
        if len(max_heap) > len(min_heap):
            return float(max_heap[0])
        else:
            return -float(min_heap[0])


def runningMedian(a):
    # Write your code here

    if len(a) == 0:
        return []
    N = len(a)
    ans = []
    min_heap = []
    max_heap = []
    for i in range(N):
        x = a[i]
        addToHeap(x, min_heap, max_heap)
        print (min_heap, max_heap)
        rebalanceHeap(min_heap, max_heap)
        print ("after rebalance: ", min_heap, max_heap)
        m = getMedian(min_heap, max_heap)
        print ("median: ", m)
        ans.append(m)
    return ans

a=[1,2,3,4,5,6,7,8,9,10]
print (runningMedian(a))