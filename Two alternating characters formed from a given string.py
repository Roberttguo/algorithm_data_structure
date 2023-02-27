'''
Given a string, remove characters until the string is made up of any two alternating characters. When you choose a
character to remove, all instances of that character must be removed. Determine the longest string possible that
contains just two alternating letters.
Example 1:

"beabeefeab"

output: 5
Explanation

The characters present in s are a, b, e, and f. This means that t must consist of two of those characters and we must
delete two others. Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].

If we delete e and f, the resulting string is babab. This is a valid t as there are only two distinct characters
 (a and b), and they are alternating within the string.

If we delete a and f, the resulting string is bebeeeb. This is not a valid string t because there are consecutive e's
present. Removing them would leave consecutive b's, so this fails to produce a valid string t.

'''
def combination(arr, start, k, tmp=[], ans=[]):
    if k==0:
        ans.append(list(tmp))
        return
    for i in range(start, len(arr)):
        tmp.append(arr[i])
        combination(arr, i+1, k-1, tmp, ans)
        tmp.pop()

def isTwoAlternating(s):
    if len(set(s))!=2:
        return False
    #assumption: s contains only two distinct chars
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            return False
    return True


def TwoAlternating(s):

    unique=list(set(s))
    ans=[]
    tmp=[]
    max_len=0
    combination(unique, 0, 2, tmp, ans)
    #print ans
    for e in ans:
        med = ""
        for i in range(len(s)):
            if s[i] in e:
                med+=s[i]
        #print med
        if isTwoAlternating(med):
            max_len=max(max_len, len(med))
            print (med)
    return max_len

s="abftanscd"
print ("max len:", TwoAlternating(s))

s="abaacdabd"
print ("max len:", TwoAlternating(s))

s="beabeefeab"
print ("max len:", TwoAlternating(s))


#print "is alternating? babab", isTwoAlternating("babab")