'''
Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring .

In one step, Alice can change a  to a  or vice versa. Count and print the minimum number of steps needed to make Alice
 see the string as beautiful.

Example


She can change any one element and have a beautiful string.

Function Description

Complete the beautifulBinaryString function in the editor below.

beautifulBinaryString has the following parameter(s):

string b: a string of binary digits
Returns

int: the minimum moves required
Input Format

The first line contains an integer , the length of binary string.
The second line contains a single binary string .
'''

#accepted! Memorize this approach
def beautifulBinaryString(b):
    # Write your code here
    if len(b)<3:
        return 0
    count=0
    while '010' in b:
        count+=1
        b=b.replace('010','011',1)
        print (b)
    return count


b='0101010'

print (beautifulBinaryString(b))

b='0100101010'

print (beautifulBinaryString(b))

b= '0100101010100010110100100110110100011100111110101001011001110111110000101011011111011001111100011101'
print (beautifulBinaryString(b))