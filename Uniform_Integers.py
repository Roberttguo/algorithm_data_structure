'''
A positive integer is considered uniform if all of its digits are equal. For example, 222222 is uniform, while 223223 is not.
Given two positive integers AA and BB, determine the number of uniform integers between AA and BB, inclusive.
Please take care to write a solution which runs within the time limit.
Constraints
1 \le A \le B \le 10^{12}1≤A≤B≤10
12

Sample test case #1
A = 75
B = 300
Expected Return Value = 5
Sample test case #2
A = 1
B = 9
Expected Return Value = 9
Sample test case #3
A = 999999999999
B = 999999999999
Expected Return Value = 1
Sample Explanation
In the first case, the uniform integers between 7575 and 300300 are 7777, 8888, 9999, 111111, and 222222.
In the second case, all 99 single-digit integers between 11 and 99 (inclusive) are uniform.
In the third case, the single integer under consideration (999{,}999{,}999{,}999999,999,999,999) is uniform.
'''


def getUniformIntegerCountInInterval(A, B):
    # Write your code here
    import math

    x = A
    n = int(math.log10(A))
    increment = 1
    for i in range(1, n + 1):
        increment += 10 ** i

    first = int(str(A)[0] * len(str(A)))
    count = 0
    x = first
    while A <= x and x <= B:
        print ("x=",x)
        count += 1
        if str(x)[0] != '9':
            x += increment
        else:
            increment += 10 ** int(math.log10(increment) + 1)
            print("inc=", increment)
            #x=int("1"*len)
            x = increment

    return count
A=75
B=300
print (getUniformIntegerCountInInterval(A, B))

A=99999999
B=999999999999
print (getUniformIntegerCountInInterval(A, B))