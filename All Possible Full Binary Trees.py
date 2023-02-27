'''
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the
answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
Example 1:

Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:

Input: n = 3
Output: [[0,0,0]]
'''

#Accepted on 3/20/2022

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n % 2 == 0:
            return []

        def helper(n, mem):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            if n in mem:
                return mem[n]
            ans = []
            for left in range(n):
                right = n - 1 - left
                leftTrees, rightTrees = helper(left, mem), helper(right, mem)

                # generate all possible combinations here from sub left trees and sub right trees
                for x in leftTrees:
                    for y in rightTrees:
                        ans.append(TreeNode(0, x, y))
            mem[n] = ans
            return ans

        mem = {}
        return helper(n, mem)