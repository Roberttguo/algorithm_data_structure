'''
This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.
'''

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mergeTwoTrees(t1,t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val=t1.val+t2.val
    '''
    m=TreeNode(t1.val+t2.val)
    if t1.left and t2.left:
        m.left = mergeTwoTrees(t1.left, t2.left)
    else:
        if t1.left:
            m.left=t1.left
        if t2.left:
            m.left= t2.left
    if t1.right and t2.right:
        m.right = mergeTwoTrees(t1.right, t2.right)
    else:
        if t1.right:
            m.right=t1.right
        if t2.right:
            m.right= t2.right
    return m
    '''
    t1.left=mergeTwoTrees(t1.left, t2.left)
    t1.right = mergeTwoTrees(t1.right, t2.right)
    return t1

def inorderTraverse(t):
    if t.left:
        inorderTraverse(t.left)
    print t.val
    if t.right:
        inorderTraverse(t.right)


t1=TreeNode(1)
t1.left=TreeNode(2)
t1.right= TreeNode(3)
t1.left.left=TreeNode(4)
t1.left.right=TreeNode(5)


t2=TreeNode(10)
t2.left = TreeNode(12)
t2.right = TreeNode(13)
t2.right.left = TreeNode(14)
t2.left.right=TreeNode(15)
print "new run:"
res=mergeTwoTrees(t1,t2)
inorderTraverse(res)
