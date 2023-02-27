'''


A
permutation
of
an
array
of
integers is an
arrangement
of
its
members
into
a
sequence or linear
order.

For
example,
for arr =[1, 2, 3], the following are considered permutations of arr: [1, 2, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1].
The
next
permutation
of
an
array
of
integers is the
next
lexicographically
greater
permutation
of
its
integer.More
formally,
if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container.If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For
example, the
next
permutation
of
arr = [1, 2, 3] is [1, 3, 2].
Similarly, the
next
permutation
of
arr = [2, 3, 1] is [3, 1, 2].
While
the
next
permutation
of
arr = [3, 2, 1] is [1, 2, 3]
because[3, 2, 1]
does
not have
a
lexicographical
larger
rearrangement.
Given
an
array
of
integers
nums, find
the
next
permutation
of
nums.

The
replacement
must
be in place and use
only
constant
extra
memory.

Example
1:

Input: nums = [1, 2, 3]
Output: [1, 3, 2]
Example
2:

Input: nums = [3, 2, 1]
Output: [1, 2, 3]
Example
3:

Input: nums = [1, 1, 5]
Output: [1, 5, 1]
'''


class Solution(object):
    def reverse(self, arr, l,r):
        while l<=r:
            arr[l],arr[r]=arr[r], arr[l]
            l+=1
            r-=1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # take [2,4,5,3,4,4,2,1] as an example 3 swap with first '4' from right, then reverse last 4 elements [4,3,2,1],
        # resulting in [2,4,5,4,1,2,3,4]

        N = len(nums)
        if N == 1:
            return

        pos = N - 2
        while pos >= 0 and nums[pos] >= nums[pos + 1]:
            pos -= 1
        #print("pos= ", pos)
        if pos < 0:  # all array is in ascending order from left to right, in this case, just need to reverse whole array
            #nums = nums[::-1] this line does not really return reversed nums, nums still in untouched.
            self.reverse(nums, 0, len(nums)-1)
            return
        # pos stops at 4th elemnt '3' for above example
        # go back to find least digit greater current '3'
        back = pos + 1
        while back < N and nums[back] > nums[pos]:
            back += 1

        # swap nums[pos] and nums[back-1]
        nums[pos], nums[back - 1] = nums[back - 1], nums[pos]
        self.reverse(nums, pos + 1, len(nums) - 1)
        #nums = nums[0:pos + 1] + nums[pos + 1:][::-1]#this way does not change original nums

o=Solution()
nums = [1,2,3]
o.nextPermutation(nums)
print ("Original nums: ", nums )
nums = [3,2,1]
o.nextPermutation(nums)
print ("Original nums: ", nums )
nums = [1,1,5]
o.nextPermutation(nums)
print ("Original nums: ", nums )

nums =[1,3,2]
o.nextPermutation(nums)
print ("Original nums: ", nums )
