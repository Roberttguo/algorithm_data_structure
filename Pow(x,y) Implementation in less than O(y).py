'''
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

Don't use recursion as it require extra space on call stack and involves function call overhead
'''

def pow(x,y):
    res = 1
    while y>0:
        if y%2>0: #odd
            res *= x
        y /= 2 #ensure log(y) so that the time complexity is O(log(y))
        x *= x #important
    return res

print pow(2,10)
print pow(2,12)