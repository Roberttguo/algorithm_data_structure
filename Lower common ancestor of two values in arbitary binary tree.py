'''

'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# following approach accepted on HackerRank, but not on leetcode, wired.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root.val==p.val or root.val==q.val:
            return root
        left=self.lowestCommonAncestor(root.left, p, q)
        right=self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
root=TreeNode(9)
root.left=TreeNode(15)
root.left.right=TreeNode(0)
root.right=TreeNode(20)
p=TreeNode(20)
root.right.left=TreeNode(11)
q=TreeNode(20)
root.right.right=TreeNode(13)

s = Solution()
res = s.lowestCommonAncestor(root,p,q)# 20, 11)
print res.val

res = s.lowestCommonAncestor(root, 15, 11)
print res.val
exit(0)
def inorder(node):
    if not node:
        return ""
    s = "("
    s += inorder(node.left)
    s += str(node.val)
    s += inorder(node.right)
    s += ")"
    print s
    return s


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

s = Solution()
res = s.lowestCommonAncestor(root, 2, 8)
print res.val

res = s.lowestCommonAncestor(root, 4, 5)
print res.val
res = s.lowestCommonAncestor(root, 3, 5)
print res.val

res = s.lowestCommonAncestor(root, 6, 9)
print res.val
res = s.lowestCommonAncestor(root, 0, 3)
print res.val

print inorder(root)