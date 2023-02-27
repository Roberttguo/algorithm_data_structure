'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an
 edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to
 pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
   1
 /  \
2    3


Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''

#Leetcode 124, Hard accepted!
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    max_path_sum = -2 ** 32

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root:
                return 0

            lsum = helper(root.left)
            rsum = helper(root.right)
            # max_cur_path inludes current node + at most its one child
            max_cur_path = max(max(lsum, rsum) + root.val, root.val)

            # Max top represents the sum when the node under
            # consideration is the root of the maxSum path and
            # no ancestor of root are there in max sum path
            max_top = max(max_cur_path, lsum + rsum + root.val)

            self.max_path_sum = max(self.max_path_sum, max_top)
            return max_cur_path

        helper(root)
        return self.max_path_sum

root=TreeNode(-10)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

o=Solution()
print (o.maxPathSum(root))