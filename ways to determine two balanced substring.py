'''
Given a string consists of '(',')','[',']', '?' only. Determine how many ways it can be split into two no-empty that is balanced.
So called 'balanced' means open bracket '[' and '(' must pair with closed bracket ']' and ')',the '?' can be '[','(',']',')'.
'''

def isBalanced(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='[' or s[i]=='(' or s[i]=='?':
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            if s[i]==']'and (stack[-1]=='[' or stack[-1]=='?'):
                stack.pop()
            if s[i]==')'and (stack[-1]=='(' or stack[-1]=='?'):
                stack.pop()
    if len(stack)%2!=0:
        return False
    while len(stack)>0 and stack[-1]=='?':
        stack.pop() #pop up '?'
        stack.pop() # pop up another one for pair
    return len(stack)==0


def howmany_ways(s):
    ways=0
    for i in range(2, len(s),2):
        s1=s[0:i]
        s2=s[i:]
        if isBalanced(s1) and isBalanced(s2):
            ways+=1
    return ways

s='[?(??)?]'

print (howmany_ways(s))

s=']?(??)?]'
print (howmany_ways(s))

