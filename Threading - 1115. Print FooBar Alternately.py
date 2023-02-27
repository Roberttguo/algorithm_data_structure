'''
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads:

thread A will call foo(), while
thread B will call bar().


Modify the given program to output "foobar" n times.



Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.


Constraints:

1 <= n <= 1000
'''
from threading import Lock
import threading

def printFoo():
    print ("foo")

def printBar():
    print ("bar")


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foolock=Lock()
        self.barlock=Lock()
        self.barlock.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foolock.acquire()
            self.barlock.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.barlock.acquire()
            self.foolock.release()
o=FooBar(5)
x=threading.Thread(target=o.foo, args=(1,))
y=threading.Thread(target=o.bar, args=(1,))
#y=threading.Thread(target=o.bar)
x.start()
y.start()