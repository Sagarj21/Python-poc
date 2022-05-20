from threading import *
def display():
    print("this display code executed by",current_thread().getName())
t=Thread(target=display)#main thred cxreqtes child thread object
t.start()#main thread stqarts child thread
print("current executing thread",current_thread().getName())







#ways of creating  thread in py
#1 creating a thread without using any class
#2 creating a thread by extending thread class
#3 creating a thread without extending  thread class