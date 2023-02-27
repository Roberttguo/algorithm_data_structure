

from collections import deque, OrderedDict

class EventFire():

    def __init__(self):
        self.queue=deque()#can be used to maintain order of callback function registration
        self.even_triggered=False

        pass


    def register(self,fun):
        self.queue.append(fun)
        if self.even_triggered:
            self.event_fire()

    def event_fire(self):
        while len(self.queue)>0:
            x=self.queue.popleft()
            x()
        self.even_triggered=True


def func1():
    print ("This is func1")

def func2():
    print ("This is func2")

def func3():
    print ("This is func3")

ef=EventFire()
ef.register(func1)
ef.register(func2)
ef.register(func2)
ef.event_fire()

ef.register(func3)
ef.register(func1)
ef.register(func2)
