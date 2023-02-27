'''
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same.
If this is not possible, return None.
'''
import heapq as Q
def Rearrange(s):
    m={}
    for x in s:
        if x in m:
            m[x]+=1
        else:
            m[x]=1
    q=[]
    for k,v in m.items():
        Q.heappush(q,[-v,k])
    ans=""
    while len(q)>1:
        first=Q.heappop(q)
        second=Q.heappop(q)
        while second[0]<0:
            ans+=first[1]+second[1]
            second[0]+=1
            first[0]+=1
        if first[0]<0:
            Q.heappush(q,first)
    if len(q)>0 and (q[0][0]<-1 or q[0][0]==-1 and ans[-1]==q[0][1]):
        return None
    return ans+q[0][1] if len(q)>0 else ans


s="aaabbc"
print (Rearrange(s))

s="aaab"
print (Rearrange(s))

s="axaab"
print (Rearrange(s))

s="xxxxxxaxaabyy"
print (Rearrange(s))