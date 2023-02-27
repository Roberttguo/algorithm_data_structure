'''
Given a string consisting of English charactoers, find first no repeating character.
'''
import collections as c

def findFirstNonRepeatingChar(s):
    d=c.OrderedDict()
    for x in s:
        if d.has_key(x):
            d[x]+=1
        else:
            d.setdefault(x,1)

    for e in d:
        if d[e]==1:
            return e
    return None
s='aaabcccdeeef'
print findFirstNonRepeatingChar(s)

s='abcbad'
print findFirstNonRepeatingChar(s)
s='abczbwadxcdxy'
print findFirstNonRepeatingChar(s)
s='abcabcabc'
print findFirstNonRepeatingChar(s)
