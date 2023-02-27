'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.



Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6


Constraints:

The numbrt of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
'''


#accepted 10/18/2021

#Note each leaf is treated as uni-value subtree???

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]

        def dfs(root, count):
            if not root:
                return True
            leftchk = dfs(root.left, count)
            rightchk = dfs(root.right, count)
            if not leftchk or not rightchk: #here we can't do like "if not dfs(root.left, count) or not dfs(root.right, count):" need to understand why
                return False

            if root.left and root.val != root.left.val:
                return False

            if root.right and root.val != root.right.val:
                return False

            count[0] += 1

            return True

        dfs(root, count)
        return count[0]



root=TreeNode(5)
root.left=TreeNode(5)
root.right=TreeNode(5)
root.left.left=TreeNode(1)
root.left.right=TreeNode(1)
root.right.left=TreeNode(2)
root.right.right=TreeNode(2)
o=Solution()
#print (o.countUnivalSubtrees2(root))
print (o.countUnivalSubtrees(root))