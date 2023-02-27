'''
invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
'''

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def invert(node):
    if not node:
        return None
    tmp=node.left
    node.left=node.right
    node.right=tmp
    invert(node.left)
    invert(node.right)
    return node

def invert_(node):#no recursion
    if not node:
        return None
    q=[node]
    while len(q)>0:
        n=q.pop()
        l=n.left
        n.left=n.right
        n.right=l
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

    return node



def preorderprint(node):#(root, left, right)
    if not node:
        return
    print node.val
    preorderprint(node.left)
    preorderprint(node.right)

def inorderprint(node): #(Left, root,right)
    if not node:
        return
    inorderprint(node.left)
    print node.val
    inorderprint(node.right)

t=TreeNode('a')
t.left=TreeNode('b')
t.right=TreeNode('c')
t.right.left=TreeNode('f')
t.left.left=TreeNode('d')
t.left.right=TreeNode('e')
inorderprint(t)
res=invert_(t)
print "after invert"
inorderprint(res)
'''
print "before invert: "
inorderprint(t)
res2=invert_(t)
print "after invert"
inorderprint(res2)
'''