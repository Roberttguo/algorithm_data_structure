'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
'''
def nthUglyNum(n):
    i2,i3,i5=0,0,0
    arr = [1]
    while len(arr) < n:
        v2,v3,v5 = arr[i2]*2, arr[i3]*3, arr[i5]*5
        m = min(v2,v3,v5)
        if m == v2:
            i2 +=1
        if m == v3:
            i3 +=1
        if m == v5:
            i5 +=1
        arr.append(m)
    return arr[-1]

print (nthUglyNum(15))