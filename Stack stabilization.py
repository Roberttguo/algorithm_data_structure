'''
Note: Chapter 2 is a harder version of this puzzle.
There's a stack of NN inflatable discs, with the iith disc from the top having an initial radius of R_iR
i
​
  inches.
The stack is considered unstable if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be stable, each disc must have a strictly smaller radius than that of the disc directly under it.
As long as the stack is unstable, you can repeatedly choose any disc of your choice and deflate it down to have a radius of your choice which is strictly smaller than the disc’s prior radius. The new radius must be a positive integer number of inches.
Determine the minimum number of discs which need to be deflated in order to make the stack stable, if this is possible at all. If it is impossible to stabilize the stack, return -1−1 instead.
Constraints
1 \le N \le 501≤N≤50
1 \le R_i \le 1{,}000{,}000{,}0001≤R
i
​
 ≤1,000,000,000
Sample test case #1
N = 5
R = [2, 5, 3, 6, 5]
Expected Return Value = 3
'''


def getMinimumDeflatedDiscCount(N, R):
    # Write your code here
    if R[N - 1] < N:
        return -1
    count = 0

    for i in range(N):
        if R[i] < i + 1:
            return -1
    stack = []
    for i in range(N):
        if len(stack) == 0:
            if R[i] > i + 1:
                stack.append(R[i])
            continue
        if stack[-1] < R[i]:
            stack.append(R[i])
        else:
            count += len(stack)
            stack = []
            if R[i] > i + 1:
                stack.append(R[i])

    return count

R = [2, 5, 3, 6, 5]
N=5

print ("res=", getMinimumDeflatedDiscCount(N, R))

R = [1, 2, 3, 6, 5]
N=5

print ("res=", getMinimumDeflatedDiscCount(N, R))
R = [1, 2, 3, 4, 5]
N=5

print ("res=", getMinimumDeflatedDiscCount(N, R))

R = [1, 1, 3, 4, 5]
N=5

print ("res=", getMinimumDeflatedDiscCount(N, R))
R = [100, 2, 33, 4, 25]
N=5

print ("res=", getMinimumDeflatedDiscCount(N, R))
