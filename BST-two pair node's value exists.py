'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such
that their sum is equal to the given target.
'''

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        inorder = set()

        def inorder_traverse(root, myset):
            if root.left:
                inorder_traverse(root.left, myset)
            #print ("node val: ", root.val)
            myset.add(root.val)
            print("set val: ", myset)
            if root.right:
                inorder_traverse(root.right, myset)
        #print (self.inorder)
        inorder_traverse(root, inorder)
        if len(inorder) < 2:
            return False
        for x in inorder:
            print ("k - x =", k - x )
            if k - x!=x and k - x in inorder:
                return True
        return False

root=TreeNode(2)
#root.left=TreeNode(3)
root.right=TreeNode(3)
'''
root.left.left=TreeNode(2)
root.left.right=TreeNode(4)
root.right.right=TreeNode(7)
'''
o=Solution()
print (o.findTarget(root,6))