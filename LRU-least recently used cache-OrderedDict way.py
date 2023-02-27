'''

'''
from collections import OrderedDict

class LRU():
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key):
        if key in self.cache:
            #self.cache.move_to_end(key)
            self.move_to_end(key)
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        self.cache[key]=value
        #self.cache.move_to_end(key)
        #self.move_to_end(key)
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)
        print self.cache

    def move_to_end(self, key):
        if key in self.cache:
            val=self.cache[key]
            self.cache.pop(key)
            self.cache[key]=val
        print self.cache

lru=LRU(4)
print lru.get(1)
lru.set(3,3)
#lru.print_dlinkedlist()
lru.set(5,5)
#lru.print_dlinkedlist()
lru.set(10,10)
#lru.print_dlinkedlist()

lru.set(20,20)
#lru.print_dlinkedlist()
print lru.get(5)
lru.set(50,50)
#lru.print_dlinkedlist()
