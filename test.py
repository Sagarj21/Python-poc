def f1():
    global a
    a=777
    print("f1",a)
def f2():
    global a
    a = 999
    print("f2",a)
def f3():
    a=1000
    print("f3",a)
f1()
f2()
f3()



#Global keyword====>to make global varialbe available to the function



