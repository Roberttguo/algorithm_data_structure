'''
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1](
here [0,n-1] is very important).

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them,
the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.



Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

'''


#accepted. Notes, the order of chunked subarrys cannot be changed when concatenating together.
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunk=0
        N=len(arr)
        sofar_sum=0 #based on index sume
        actual_sum=0
        #after chunking, each chunked subarray's sum must be eual to the corresponding sum of original array got sorted. arr is from 0 to n-1, sofar sum is related to index
        for i in range(N):
            sofar_sum+=i
            actual_sum+=arr[i]
            if sofar_sum==actual_sum:
                chunk+=1
        return chunk

