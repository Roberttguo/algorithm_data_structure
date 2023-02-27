'''
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the
following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
'''

#following solution is for python3, python2 does not have method 'move_to_end() in OrderedDict
from collections import OrderedDict

class LRU():
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        self.cache[key]=value
        self.cache.move_to_end(key)
        if len(self.cache)>=self.capacity:
            self.cache.popitem(last=False)

##############################################

class DoubleLinkedListNode():
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.pre=None
        self.next=None


class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache={}
        self.head=DoubleLinkedListNode(0,0)
        self.tail=DoubleLinkedListNode(0,0)
        print (self.head, self.tail)
        self.head.next=self.tail
        self.tail.pre=self.head

    def _delete(self, node): #without delete it from memory
        #delete current node
        pre=node.pre
        next=node.next
        pre.next=next
        next.pre=pre

    #any insertion to double linked list involves 4 operations(4 connection operation)
    def _move_to_end(self, node):
        cur=self.tail
        cur.pre.next=node
        node.pre=cur.pre
        node.next=self.tail
        self.tail.pre=node #can't forget here
        #print "tail's pre: ", cur.pre, cur.pre.key, cur.pre.val, "head's next: ", self.head.next.key, self.head.next.val, "tail's pre and tail itself:", self.tail.pre.key, self.tail.key

    def remove_head(self):
        cur=self.head
        node=cur.next
        cur.next=node.next
        node.next.pre=cur
        #del(node)
        self.head = cur

    def update(self, node):
        self._delete(node)
        #move current node to front of tail, insert to fron of original tail
        self._move_to_end(node)


    def get(self, key):
        if key in self.cache:
            n=self.cache[key]
            self.update(n)
            val=n.val
            return val
        else:
            return -1

    def set(self, key, val):
        if key in self.cache:
            old=self.cache[key]
            self._delete(old)
        n=DoubleLinkedListNode(key,val)
        self.cache[key]=n
        self._move_to_end(n)
        if len(self.cache)>=self.capacity:
            self.cache.pop(self.head.next.key)
            self.remove_head()

    def print_dlinkedlist(self):

        node =self.head
        while node:
            print ("key= ", node.key, "val= ", node.val)
            node=node.next
        print ("end", self.cache)


lru=LRUCache(4)
print (lru.get(1))
lru.set(3,3)
lru.print_dlinkedlist()
lru.set(5,5)
lru.print_dlinkedlist()
lru.set(10,10)
lru.print_dlinkedlist()

lru.set(20,20)
lru.print_dlinkedlist()
lru.get(5)
lru.set(50,50)
lru.print_dlinkedlist()



