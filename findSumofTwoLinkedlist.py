'''
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
'''

class ListNode():
    def __init__(self, val):
        self.val=val
        self.next = None

def sum(l1,l2):
    """
    :param l1:ListNode
    :param l2: ListNode
    :return: ListNode
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    dummy=ListNode(0)
    worker = dummy
    carry = 0
    while l1 and l2:
        sum = (l1.val+l2.val+carry)%10
        worker.next = ListNode(sum)
        worker = worker.next
        if l1.val+l2.val+carry>=10:
            carry = 1
        else:
            carry = 0
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    while l1:
        sum = (l1.val+carry)%10
        worker.next = ListNode(sum)
        worker = worker.next
        if l1.val +carry >= 10:
            carry = 1
        else:
            carry = 0
        if l1:
            l1 = l1.next

    while l2:
        sum = (l2.val+carry)%10
        worker.next = ListNode(sum)
        worker = worker.next
        if l2.val +carry >= 10:
            carry = 1
        else:
            carry = 0
        if l2:
            l2 = l2.next
    if carry>0:
        worker.next = ListNode(1)
    return dummy.next

def revere(l):
    if l is None:
        return l
    dummy = ListNode(0)
    worker = dummy
    while l:
        tmp=worker.next
        worker.next = l
        print worker.next.val
        worker.next.next = tmp
        #worker = worker.next
        l=l.next
        if l:
            print "next node's val:",l.val
    return dummy.next
import copy
def printllist(l):
    q=[]
    node=copy.copy(l)
    while node:
        q.append(node.val)
        node=node.next
    print q

l1=ListNode(9)
l1.next=ListNode(9)

l2=ListNode(5)
l2.next=ListNode(2)

s = sum(l1,l2)
printllist(s)

l1=ListNode(9)
l1.next=ListNode(9)
l1.next.next=ListNode(8)
l2=ListNode(5)
l2.next=ListNode(2)

s = sum(l1,l2)
printllist(s)

l1=ListNode(9)
l1.next=ListNode(9)
l1.next.next=ListNode(9)
l2=ListNode(5)
l2.next=ListNode(2)

s = sum(l1,l2)
print 'sum='
printllist(s)

r = revere(s)
printllist(r)
