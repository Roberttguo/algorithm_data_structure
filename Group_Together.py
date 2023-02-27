"""
abc
' <=> '
bcd
' <=> '
efg
' <==> '
xyz
' <=> '
zab
'
1
1
'acd' <= > 'bde' <= > 'cef'

input: ['abc', 'bcd', 'bde', 'cef']

output: [['abc', 'bcd'], ['bde', 'cef']]

"""

def shift(s,n):
    ans=""
    map_tbl=[chr(ord('a')+i) for i in range(26)]
    #print (map_tbl)
    n=n%26
    N=len(s)
    ans=""
    for i in range(N):
        pos=ord(s[i])-ord('a')
        pos_=(pos+n)%26
        ans+=map_tbl[pos_]
    return ans


    #return ans

def group(arr):
    if len(arr)<1:
        return []
    if len(arr)==1:
        return [[arr[0]]]
    ans=[]#set()
    tmp=[]
    mem={}
    for w in arr:
        mem.setdefault(w,[])
    seen={}
    for w in arr:

        for i in range(1,26):
            shifted=shift(w, i)
            #if shifted not in seen and shifted in mem:
            if shifted in mem:
                mem[w].append(shifted)
        seen[w]=1

    for k,v in mem.items():
        v.append(k)
        v.sort()
        #tmp.append(x)
        if v not in ans:
            ans.append(v)
    return ans#list(ans) #[mem.values()]

#O(N*26*maxLenofWord)
arr=['abc', 'bcd', 'bde', 'cef']

print (group(arr))