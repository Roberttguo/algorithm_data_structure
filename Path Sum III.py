'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values
along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from
parent nodes to child nodes).



Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
Accepted
295,220
Submissions
603,553
'''


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):

    #this hashmap way does not seem to work for some cases
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        m={0:1}#initialize for case that node val just equal to targetSum

        def helper(node, runningsum, targetSum, m):
            if not node:
                return 0
            count=0
            runningsum+=node.val
            if runningsum in m:
                m[runningsum] += 1
            else:
                m[runningsum] = 1
            #print "runningsum:", runningsum, count
            if runningsum-targetSum in m:
                #print "runningsum in cache:", count, m[ runningsum-targetSum]
                count=m[ runningsum-targetSum]

            count+=helper(node.left, runningsum, targetSum,m)+helper(node.right, runningsum,targetSum,m)
            if runningsum in m:
                m[runningsum]-=1
                if m[runningsum]==0:
                    m.pop(runningsum)
            return count
        return helper(root,0, targetSum, m)


    def pathSum_2f(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0


        def helper(node, targetSum):
            res=0
            if not node:
                return 0
            if node.val==targetSum:
                res=1
            res+=helper(node.left, targetSum-node.val)
            res+=helper(node.right, targetSum-node.val)
            return res
        return self.pathSum_2f(root.left, targetSum)+helper(root, targetSum)+self.pathSum_2f(root.right, targetSum)

root=TreeNode(1)
root.right=TreeNode(2)
root.right.right=TreeNode(3)
root.right.right.right=TreeNode(4)
root.right.right.right.right=TreeNode(5)
o=Solution()
print o.pathSum(root, 3)
print o.pathSum_2f(root, 3)
root=TreeNode(1)
print o.pathSum(root, 0)
print o.pathSum_2f(root, 0)