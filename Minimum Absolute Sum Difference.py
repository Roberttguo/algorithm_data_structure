'''
You are given two positive integer arrays nums1 and nums2, both of length n.

The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

|x| is defined as:

x if x >= 0, or
-x if x < 0.


Example 1:

Input: nums1 = [1,7,5], nums2 = [2,3,5]
Output: 3
Explanation: There are two possible optimal solutions:
- Replace the second element with the first: [1,7,5] => [1,1,5], or
- Replace the second element with the third: [1,7,5] => [1,5,5].
Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.
Example 2:

Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
Output: 0
Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an
absolute sum difference of 0.
Example 3:

Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
Output: 20
Explanation: Replace the first element with the second: [1,10,4,4,2,7] => [10,10,4,4,2,7].
This yields an absolute sum difference of |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
'''
#My way seems to work at first glane,actually after finding an element in nums2 corresponding to the max abs, then find closet element in nums1 to it, which does not gurantee minimum result.
# Correct way (1) find total absolute diff and create such diff array (2) sort first array, iterate second array and find each ele's pos in sorted firt arra and obtain min diff to its adjacent elements, store it to best_diff array
#(3)scan diff array and best diff array to find max diff that can result in minimum diff sum

import bisect # or use binary search to create my own method to find a pos in sorted array for a given element

def minAbsoluteSumDiff(nums1, nums2):

    diff_sum=0
    diff=[]
    n=len(nums1)
    for i in range(n):
        x=abs(nums1[i]-nums2[i])
        diff_sum+=x
        diff.append(x)
    if diff_sum==0:
        return diff_sum
    #as to each element in nums2, find an element in nums1 via binary search that is closet to it to result in minimum diff, then compare original diff array, the max one is correspond to one that should be replaced in nums1
    best_diff=[] #
    nums1.sort()

    for i in range(n):
        idx=bisect.bisect_left(nums1, nums2[i])
        min_diff=2**32
        if idx>0 and idx<n:
            min_diff=min(abs(nums1[idx]-nums2[i]), abs(nums1[idx-1]-nums2[i]))
        else:#idx=0 or idx=n, note idx never be zero
            if idx==0:
                min_diff = abs(nums1[idx] - nums2[i])
            if idx==n:
                min_diff = abs(nums1[idx-1] - nums2[i])
        best_diff.append(min_diff)
    print (diff, best_diff)
    #save_diff=0
    max_save=0
    for i in range(n):
        save_diff=abs(diff[i]-best_diff[i])
        max_save=max(max_save, save_diff)
    print (max_save)
    return int((diff_sum-max_save)%(10**9+7))

nums1=[1,7,5]
nums2=[2,3,5]

print (minAbsoluteSumDiff(nums1, nums2))

nums1=[10,7,3,5,60]
nums2=[2,3,5,1,0]
print (minAbsoluteSumDiff(nums1, nums2))