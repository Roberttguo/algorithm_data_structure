'''
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
678 is not a palindrome. Do not convert the integer into a string.
'''
import math


def isPalindrome(x):
    if x<0:
        x=-x
    N = int(math.log10(x))
    if N == 0:
        return True

    while x>9:
        y=int(math.pow(10,N))
        print "y=",y
        if x/y!= x%10:
            return False
        x=int((x%y)/10)
        print "x=",x
        N-=2 #pay attention here, should decrease 2
    return True

print isPalindrome(121)

print isPalindrome(12341)
print isPalindrome(12321)
print isPalindrome(-55555)
print isPalindrome(-5555)