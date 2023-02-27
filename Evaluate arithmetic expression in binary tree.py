class TreeNode():
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
#not submitted to leetcode, but seems to work.
class Solution():

    def evaluate(self, root):
        return self.helper(root)

    def calculate(self,x,op,y):
        #print ("x=", x, "y=",y)
        if op=="+":
            return int(x)+int(y)
        if op=="*":
            return int(x)*int(y)
        if op=="-":
            return int(x)-int(y)
        if op=="/":
            return int(x)/int(y)

    def helper(self, root):
        if not root:
            return 0
        if root.val not in ["+","-", "/","*"]:
            return int(root.val)
        left_val=self.helper(root.left)
        right_val=self.helper(root.right)

        return self.calculate(left_val, root.val, right_val)


root=TreeNode("*")
root.left=TreeNode("+")
root.right=TreeNode("+")
root.left.left=TreeNode(3)
root.left.right=TreeNode(2)
root.right.left=TreeNode("/")
root.right.left.left=TreeNode(27)
root.right.left.right=TreeNode(3)
root.right.right=TreeNode("-")
root.right.right.left=TreeNode("10")
root.right.right.right=TreeNode("*")
root.right.right.right.left=TreeNode("2")
root.right.right.right.right=TreeNode("/")
root.right.right.right.right.left=TreeNode("100")
root.right.right.right.right.right=TreeNode("5")
o=Solution()
print (o.evaluate(root))