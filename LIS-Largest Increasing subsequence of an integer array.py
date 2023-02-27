'''

The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

'''
#typical quiz, can be reused for "leetcode 368  Largest Divisible Subset"
def LIS(nums):
    N=len(nums)
    lis=[1]*N #dp transit matrix, at least 1 is minmum largest increasing sebsequence

    for i in range(1, N):
        for j in range(i):
            if nums[i]>nums[j] and lis[i]<lis[j]+1:
                lis[i]=lis[j]+1
    max_len=0
    for i in range(N):
        max_len=max(max_len, lis[i])
    return max_len

nums=[10, 22, 9, 33, 21, 50, 41, 60, 80]

print (LIS(nums))
nums=[10, 22, 23, 33, 21, 50, 51, 60, 80]

print (LIS(nums))