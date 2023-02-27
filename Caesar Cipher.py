'''
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
Example


The alphabet is rotated by , matching the mapping above. The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string
Input Format

The first line contains the integer, , the length of the unencrypted string.
The second line contains the unencrypted string, .
The third line contains , the number of letters to rotate the alphabet by.


'''

def caesarCipher(s, k):
    # Write your code here
    k=k%26
    cipher=""
    for i in range(len(s)):
        if not (s[i].islower() or s[i].isupper()):
            cipher+=s[i]
        else:
            if s[i].isupper():
                if ord(s[i])+k>ord('Z'):
                    cipher+=chr(ord('A')-1+(ord(s[i])+k)%ord('Z'))
                else:
                    cipher+=chr(ord(s[i])+k)
            else:
                if ord(s[i])+k>ord('z'):
                    cipher+=chr(ord('a')-1+(ord(s[i])+k)%ord('z'))
                else:
                    cipher+=chr(ord(s[i])+k)
    return cipher

s="www.abc.xy"
k=87

print caesarCipher(s,k)
print (ord('w')+k)%ord('z')
print chr(84), 87%26