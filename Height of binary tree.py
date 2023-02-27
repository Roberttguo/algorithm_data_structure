class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right=None
        self.left=None

def height(root):
    if not root or root.left==None and root.right==None:
        return 0
    lh= height(root.left)+1
    rh=height(root.right)+1
    return max(lh, rh)

root=TreeNode(3)
root.left=TreeNode(2)
root.left.left=TreeNode(1)
root.right=TreeNode(5)
root.right.left=TreeNode(4)
root.right.right=TreeNode(6)
root.right.right.right=TreeNode(7)
root.right.right.right.left=TreeNode(8)
root.right.right.right.right=TreeNode(9)
root.right.right.right.right.right=TreeNode(10)
print height(root)