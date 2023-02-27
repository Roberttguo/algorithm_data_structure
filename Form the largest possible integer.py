'''
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
'''

class customeInt():
    def __init__(self, val):
        self.val=val

    def __gt__(self, other):#always compare self.val to other
        print "first great than second! first is:", self.val
        M = len(str(self.val))
        N = len(str(other.val))
        if M==N:
            return str(self.val)[0:M]>str(other.val)[0:M]
        else:#M!=N
            min_len=min(M,N)
            if str(self.val)[0:min_len]>str(other.val)[0:min_len]:
                return True
            elif str(self.val)[0:min_len]<str(other.val)[0:min_len]:
                return False
            else: #str(self.val)[0:min_len]==str(other.val)[0:min_len]
                if M>N:
                    j=N
                    while j<M:
                        if str(self.val)[j]<str(other.val)[N-1]:
                            return False
                        j+=1
                    return True
                if M<N: # and str(self.val)[M-1]>str(other.val)[M]:
                    j=M
                    while j<N:
                        if str(self.val)[M-1]<str(other.val)[j]:
                            return False
                        j+=1
                    return True


    def __eq__(self, other):
        print "both equal!"
        M = len(str(self.val))
        N = len(str(other.val))
        if M==N:
            return str(self.val)[0:M]==str(other.val)[0:M]
        return False

    def __lt__(self, other):#other is the instance of this class itself.
        M = len(str(self.val))
        N = len(str(other.val))
        if M==N:
            return str(self.val)[0:M]<str(other.val)[0:M]
        else:#M!=N
            min_len=min(M,N)
            if str(self.val)[0:min_len]<str(other.val)[0:min_len]:
                return True
            elif str(self.val)[0:min_len]>str(other.val)[0:min_len]:
                return False
            else: #str(self.val)[0:min_len]==str(other.val)[0:min_len]
                if M>N:
                    j=N
                    while j<M:
                        if str(self.val)[j]>str(other.val)[N-1]:
                            return False
                        j+=1
                    return True
                if M<N:
                    j=M
                    while j<N:
                        if str(self.val)[M-1]>str(other.val)[j]:
                            return False
                        j+=1
                    return True


arr=[10,7,76,415]

mid=map(customeInt,arr)
mid.sort()
for i in range(len(mid)):
    print mid[i].val
j=len(mid)-1
ans=""
while j>=0:
    ans+=str(mid[j].val)
    j-=1
print int(ans)

arr=[10,7,788,415,776]

mid=map(customeInt,arr)

print "New test:"
mid.sort()
for i in range(len(mid)):
    print mid[i].val
j=len(mid)-1
ans=""
while j>=0:
    ans+=str(mid[j].val)
    j-=1
print int(ans)
