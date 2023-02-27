#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
class SinglyLinkedListNode():
    def __init__(self, data):
        self.data = data
        self.next = None
#test passed at Hackerrank
def mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    dummy=SinglyLinkedListNode(0)
    worker=dummy
    while head1 or head2:
        if not head1:
            worker.next=head2
            break
        if not head2:
            worker.next = head1
            break
        if head1.data>=head2.data:
            tmp=head2.next
            worker.next=head2
            head2.next=None
            worker=worker.next
            head2=tmp
        else:
            tmp = head1.next
            worker.next=head1
            head1=None
            worker=worker.next
            head1=tmp
    return dummy.next
