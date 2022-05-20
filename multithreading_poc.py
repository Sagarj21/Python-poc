from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("child thread 1 executed by",current_thread().getName())
obj=Test()
t1=Thread(target=obj.display)
t2=Thread(target=obj.display)
t3=Thread(target=obj.display)
t4=Thread(target=obj.display)
t5=Thread(target=obj.display)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
for i in range(10):
    print("main thread")





#ways of creating  thread in py
#1 creating a thread without using any class
"""from threading import *
def display():
    for i in range(10):
        print("child thread")
t=Thread(target=display)#main thred cxreqtes child thread object
t.start()#main thread stqarts child thread
for i in range(10):
    print("main thread")"""
#2 creating a thread by extending thread class  ??highly recommended method
#self is like this keyword n java  pointer to current object,thread functionality should be specified in run menthod
"""from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("child thread 1")
t=MyThread()
t.start()
for i in range(10):
    print("main thread 1")"""
#3 creating a thread without extending  thread class
"""from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("child thread 1")
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("main thread")"""

