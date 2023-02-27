
class TreeNode():
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def count(root):

    def count_height(root):
        if not root:
            return 0
        return count_height(root.left)+1


    def count_right(root, row):
        if not root:
            return 0
        row[0] +=1
        return count_right(root.right,row )
    row=[0]
    count_right(root, row)
    print ("right row: ", row[0])
    return count_height(root)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(4)
root.right.left=TreeNode(5)

print (count(root))