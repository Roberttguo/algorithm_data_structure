
def combination(arr, k, start, mid, res):

    if k==0:
        #res.append("".join(mid))
        res.append(list(mid))
        #print res
    for i in range(start, len(arr)):
        mid.append(arr[i])
        combination(arr,k-1, i+1, mid, res)#i+1 avoid duplicates, instead of start+1
        mid.pop()
    return res

arr=['a','b','c','d','e','f']
mid=[]
res=[]
for m in range(1, len(arr)):
    print (combination(arr,m,0, mid, res))

print ("res=? ", res)
def isValidAlternating(s):
    i = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            return False
        i += 1
    return True

s='abab'
print (isValidAlternating(s))
'''
s='ababa'
print isValidAlternating(s)
s='ababba'
print isValidAlternating(s)
s='abababaa'
print isValidAlternating(s)
'''