'''
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''

def merge_interval(l):
    if len(l)<=1:
        return l
    l.sort()
    res=[l[0]]
    i=1
    while i <len(l):
        if res[-1][1]<l[i][0]:
            res.append(l[i])
        else:
            if res[-1][1]>=l[i][1]:#skip a overlapped element
                i+=1 #must have this line, or endless loop
                continue
            tmp=res.pop()
            t=(tmp[0],l[i][1])# because tuple is immutable, redefine a new tuple
            #print "new tuple:", t
            res.append(t)
            #print "append a new tuple:", res
        i+=1
    return res

#l=[[0, 3], [1, 7], [2, 1], [2, 3], [2, 7], [3, 4]]
l=[(0, 3), (1, 7),(2, 3), (2, 7), (3, 4)]
print merge_interval(l)

l2=[(1, 3), (5, 8), (4, 10), (20, 25)]
print merge_interval(l2)