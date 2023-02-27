class Node(object):

    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None


root=Node(9)
root.left=Node(3)
root.right=Node(2)
root.left.left=Node(4)
root.left.right=Node(1)
root.right.right=Node(6)
ans=[]
def preOrder(root, ans):
    if not root:
        ans.append(",#")
        return
    if len(ans)==0:
        ans.append(str(root.val))
    else:
        ans.append(","+str(root.val))
    preOrder(root.left,ans)
    preOrder(root.right, ans)


preOrder(root, ans)
print ("answer is :", "".join(ans))

s="9,3,4,#,#,1,#,#,2,#,6,#,#"
arr=s.split(",")
print ("arr=", arr)

idx = [0]


def isValid(arr, idx):
    if idx[0] >= len(arr):
        return False
    if arr[idx[0]] == "#":
        return True  # why? first root can be None->#
    idx[0] += 1  # point to left child
    left = isValid(arr, idx)
    idx[0] += 1  # point to right child
    right = isValid(arr, idx)
    return left and right
print ("valid?", isValid(arr, idx), idx[0])