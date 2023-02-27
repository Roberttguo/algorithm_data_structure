'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the
list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

#Leetcode 114. Flatten Binary Tree to Linked List

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Aceepted on 11/8/2021, recall this apporach
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root or root.left==None and root.right==None:
            return
        node=root
        while node.left or node.right:
            if node.left==None:
                node=node.right
                #continue
            else:
                backup=node # after connecting node's left, this is used to iterate to most right node within connected original left node
                tmp=node.right
                node.right=node.left
                node.left=None #important
                #root=root.right
                while backup.right:
                    backup=backup.right
                backup.right=tmp
                node=node.right
        return