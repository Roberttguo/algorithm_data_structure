'''
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.



Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11


Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000
'''

'''
Algorithm:
We first get the count of each answer from rabbit.
The rabbit number of each group are "answer+1", and we need to get the number of groups for this answer[i ]+1:
total rabbits saying the same answer/(the answer+1)=>groups.
That count (groups) divided by "answer+1" is the number of each group. If there is remainder, the group should add 1.
So the minimum number of rabbits are each "answer+1" multiply the group number.

'''


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        mem = {}
        for x in answers:
            if x in mem:
                mem[x] += 1
            else:
                mem[x] = 1
        groups = 0

        ans = 0
        for k, v in mem.items():
            group = v / (k + 1)
            if v % (k + 1) != 0:
                group += 1
            ans += (k + 1) * group

        return ans