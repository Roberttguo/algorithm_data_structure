'''

'''


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

##### Pay Attention!!!##################
####Top view and bottom view are actually vertically traversal's view from top and from bottom
#### In Python3, dict.keys() is not a list, in Python2, it is
class Node():
    def __init__(self, data):
        self.info=data
        self.left = None
        self.right = None

def topView(root):
    # Write your code here
    if not root:
        return
    #col = 0
    pre_left, pre_right = 0, 0
    Q = [(root, 0)]
    ans = [root.info]
    level = 0

    while len(Q) > 0:
        size = len(Q)
        if size > 1 and level > 0:
            print (Q)
            print ("pre_left: pre_right", pre_left, pre_right, Q[0][0].info, Q[0][1], Q[-1][0].info, Q[-1][1])
            if Q[0][1] < pre_left:
                ans.append(Q[0][0].info)
                pre_left -= 1
            if Q[-1][1] > pre_right:
                ans.append(Q[-1][0].info)
                pre_right += 1
        elif level > 0 and size == 1:
            if Q[0][1] < pre_left or Q[0][1] > pre_right:
                ans.append(Q[0][0].info)
                if Q[0][1] < pre_left:
                    pre_left -= 1
                if Q[0][1] > pre_right:
                    pre_right += 1
        for _ in range(size):
            tmp = Q.pop(0)
            if tmp[0].left:
                Q.append((tmp[0].left, tmp[1]-1))
            if tmp[0].right:
                Q.append((tmp[0].right, tmp[1]+1))
        level += 1
    out = " ".join(map(str, ans))
    print (out)

def deepestNode(root):

    stack=[root]
    prelevel=-1
    level=0
    deepestNode=None
    while len(stack)>0:
        size=len(stack)
        for _ in range(size):
            node=stack.pop()
            if node.left==None and node.right==None and prelevel<level:
                deepestNode=node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        level+=1
    return deepestNode.info

from collections import deque
def topview_firstVeritical(root):
    if not root:
        return None
    top={}
    bot={}
    col=0
    Q=deque()
    Q.append((root, col))
    while Q:
        size=len(Q)
        for _ in range(size):
            tmp=Q.popleft()
            if tmp[1] not in top:
                top[tmp[1]]=tmp[0].info
            #if tmp[1] not in bot:
            bot[tmp[1]]=tmp[0].info

            if tmp[0].left:
                Q.append((tmp[0].left, tmp[1]-1))
            if tmp[0].right:
                Q.append((tmp[0].right, tmp[1]+1))

    print (top, bot)
    items=list(top.items())
    items.sort()
    ans=[x for y, x in items]

    items2=list(bot.items())
    items2.sort()
    ans2=[x for y, x in items2]

    return ans, ans2




root=Node(1)
root.right=Node(2)
root.left=Node(-2)
root.left.left=Node(-5)
root.left.right=Node(25)
root.right.right=Node(5)
root.right.right.left=Node(3)
root.right.right.right=Node(6)
root.right.right.left.right=Node(4)

topView(root)
print ("top view:", topview_firstVeritical(root))
print (deepestNode(root))