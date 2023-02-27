def zigzag(s, k):
    ans=[[" "]*len(s) for _ in range(k)]
    row=0
    down=True
    for i in range(len(s)):
        ans[row][i]=s[i]
        if down:
            row+=1
        else:
            row-=1
        if row==k-1:
            down=False
        if row==0:
            down=True
    return ans

#print len('a   e   ')
s="abcdefghix"
k=3
res=zigzag(s, 3)
for i in range(len(res)):
    #print res[i]
    print " ".join(res[i])

