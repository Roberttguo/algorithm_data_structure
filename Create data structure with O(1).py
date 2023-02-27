'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Create a data structure that performs all the following operations in O(1) time:

plus: Add a key with value 1. If the key already exists, increment its value by one.
minus: Decrement the value of a key. If the key's value is currently 1, remove it.
get_max: Return a key with the highest value.
get_min: Return a key with the lowest value.
'''

class LeastOperation():
    def __init__(self):
        self.cache={}
        self.max=None
        self.min=None

    def plus(self,key):
        if self.cache.has_key(key):
            self.cache[key]+=1
        else:
            self.cache[key]=1
        if self.max==None:
            self.max=(self.cache[key],key)
        else:
            self.max=max(self.max, (self.cache[key], key))
        if self.min==None:
            self.min=(self.cache[key],key)

    def minus(self,key):


    def get_max(self):
        if self.max:
            return self.max[1]
        return None

    def get_min(self):
        if self.min:
            return self.min[1]
        return None