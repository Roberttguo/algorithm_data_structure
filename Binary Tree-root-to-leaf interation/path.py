'''
Given the root of a binary tree, return all root-to-leaf paths in any order.
'''

#Accepted on 2/9/2022. Attention: when reaching a leaf node, print.Back tracking happens at last line

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        tmp = []
        if not root:
            return [""]

        def dfs(root, tmp, ans):
            if not root:
                return
            tmp.append(str(root.val))
            if root.left == None and root.right == None:
                ans.append("->".join(tmp))
            dfs(root.left, tmp, ans)
            dfs(root.right, tmp, ans)
            tmp.pop()# hack tracking is here, not any line above

        dfs(root, tmp, ans)
        return ans