'''
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the
node's value. If it is a null node, we record using a sentinel value such as '#'.


For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.



Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: preorder = "1,#"
Output: false
Example 3:

Input: preorder = "9,#,#,1"
Output: false
'''

#Accepted on 2/9/2022
# The idea here is to traverse in a pre-order manner, and ensure all indexes were met, while all subtrees are valid binary trees.

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        arr = preorder.split(",")
        size = len(arr)
        idx = [0]

        def isValid(arr, idx):
            if idx[0] >= len(arr):
                return False
            if arr[idx[0]] == "#":
                return True  # why? first root can be None-># IMPORT line here!!!!!
            idx[0] += 1  # point to left child
            left = isValid(arr, idx)
            idx[0] += 1  # point to right child
            right = isValid(arr, idx)
            return left and right

        return isValid(arr, idx) and idx[0] == len(arr) - 1