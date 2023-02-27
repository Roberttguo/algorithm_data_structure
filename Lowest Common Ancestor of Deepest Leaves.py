'''
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in
the subtree with root A.


Example 1:

       3
    /    \
   5      1
 /  \    /  \
6   2   0    9
   / \
7     4


'''

#Accepted by leetcode 2/8/2022
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        def depth(root):
            if not root:
                return (0, None)
            l = depth(root.left)
            r = depth(root.right)
            dl = l[0]
            dr = r[0]
            if dl == dr:
                return (max(dl, dr) + 1, root)
            else:
                if dl > dr:
                    return (dl + 1, l[1])
                else:
                    return (dr + 1, r[1])

        return depth(root)[1]