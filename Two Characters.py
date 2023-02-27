'''
Given a string, remove characters until the string is made up of any two alternating characters. When you choose a
character to remove, all instances of that character must be removed. Determine the longest string possible that
contains just two alternating letters.

Example


Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4.
Removing either b or d at any point would not result in a valid string. Return .

Given a string , convert it to the longest possible string  made up only of alternating characters.
Return the length of string . If no string  can be formed, return .

Function Description

Complete the alternate function in the editor below.

alternate has the following parameter(s):

string s: a string
Returns.

int: the length of the longest valid string, or  if there are none
Input Format

The first line contains a single integer that denotes the length of .
The second line contains string .

Constraints

Sample Input

STDIN       Function
-----       --------
10          length of s = 10
beabeefeab  s = 'beabeefeab'
Sample Output

5
Explanation

The characters present in  are a, b, e, and f. This means that  must consist of two of those characters and
we must delete two others. Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].

If we delete e and f, the resulting string is babab. This is a valid  as there are only two distinct characters (a and b),
 and they are alternating within the string.

If we delete a and f, the resulting string is bebeeeb. This is not a valid string  because there are consecutive e's present.
Removing them would leave consecutive b's, so this fails to produce a valid string .

Other cases are solved similarly.

babab is the longest string we can create.
'''
def combination(arr,k, start_index, mid, ans):
    if k==0: # already pickup k elements from arr
        ans.append(list(mid))

    for i in range(start_index,len(arr)):
        mid.append(arr[i])
        combination(arr, k-1, i+1, mid, ans) #instead of start_index+1, should be i+1 here
        mid.pop()


#Navie approach:
def alternate(s):
    # Write your code here
    #(1) find all unique chars
    distinct =set(list(s))

    #(2) find all combinations of pick 2 from distinct
    arr=list(distinct)
    ans=[]
    mid=[]
    combination(arr, 2, 0, mid, ans)
    #(3) iterate all possible two elements to form valid alternate string
    max_len=0
    for x in ans:
        #print x
        stack = []
        for i in range(len(s)):
            if s[i] not in x:
                continue
            if len(stack)==0 or stack[-1]!=s[i]:
                stack.append(s[i])
            else:
                stack = []
                break
        print "packed: ", stack, "".join(stack)
        max_len = max (max_len, len(stack))
    return max_len

s = 'beabeefeab'
print alternate(s)

s = 'xxxxwyyyuv'
print alternate(s)