'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat
 numbers, k. For example, there will not be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''

#Finally accepted on 12/26/2021
#pay attend to writing back tmp to stack, char by char instead of a wolly string
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def append2Stack(st,string):
            for i in range(len(string)):
                st.append(string[i])


        ans = ""
        stack = []
        for x in s:
            if x != ']':
                stack.append(x)
            else:
                tmp = ""
                while len(stack) > 0 and stack[-1] != '[':
                    tmp += stack.pop()
                stack.pop()  # remove '['
                digit = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    digit += stack.pop()

                if len(digit) > 0:
                    k = int(digit[::-1])
                    append2Stack(stack, k * tmp[::-1])

        ans="".join(stack)
        return ans




#another try using different stack for '[', digit, regular char

def decode(s):
    char_stack=[]
    bracket_stack=[]
    digit_stack=[]
    tmp=""
    i=0
    N=len(s)
    while i<N:
        x=s[i]
        if x.isdigit():
            digit=x
            #likely more than one digit
            k=i+1
            while s[k].isdigit():
                digit+=s[k]
                k+=1
            digit_stack.append(int(digit))
            i=k
            continue
        if x=='[':
            bracket_stack.append(x)
            i+=1
            continue
        if x==']':
            print ("char_stack: ", char_stack)
            m=digit_stack.pop()
            t=char_stack.pop()
            bracket_stack.pop()
            if len(char_stack)>0 and len(digit_stack)!=0: #and len(digit_stack)==0 and len(bracket_stack)==0:
                char_stack.append(t * m)
                #char_stack[-1]+=t*m
            else:
                #char_stack.append(t*m)
                if len(char_stack)>0:
                    char_stack[-1] += t * m
                else:
                    char_stack.append(t * m)
            print("char_stack: ", char_stack)
            i+=1
            continue
        else:
            tmp+=x
            k=i+1
            while k<N and s[k]!='[' and s[k]!=']' and not s[k].isdigit():
                tmp+=s[k]
                k+=1
            i=k
            char_stack.append(tmp)
            tmp=""

    return "".join(char_stack)
s = "3[a]2[bc]"

o=Solution()
'''
print (o.decodeString(s))
print (decode(s))


s="100[leetcode]"
print (o.decodeString(s))
print (decode(s))

s="3[a2[c]]"
print (o.decodeString(s))
print (decode(s))
'''
s="3[z]2[2[y]pq4[2[jk]e1[f]]]ef"  #expected: "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

print (o.decodeString(s))
print (decode(s))

exit()
s = "2[abc]3[cd]ef"
print (o.decodeString(s))
print (decode(s))


s="abc3[cd]xyz"
print (o.decodeString(s))
print (decode(s))