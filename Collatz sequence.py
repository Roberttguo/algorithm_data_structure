'''
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
'''

ans=[]
def collatzSequence(n, ans):
    if n == 1:
        return
    if n%2==0:
        ans.append(n/2)
        collatzSequence(n/2, ans)
    else:
        ans.append(3*n+1)
        collatzSequence(3*n+1, ans)

ans=[]
collatzSequence(2,ans)
print ans
#exit(0)
ans=[]
collatzSequence(5,ans)
print ans

ans=[]
collatzSequence(11,ans)
print ans

ans=[]
collatzSequence(24,ans)
print ans

ans=[]
collatzSequence(1,ans)
print ans