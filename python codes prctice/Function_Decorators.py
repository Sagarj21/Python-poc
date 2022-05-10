#function decorators::
#decorators help to make our code shorter and more pythonic
def decor(func):
    def inner(name):
        if name=='sunny':
            print("hello sunny bad morining")
        else:
            func(name)
    return inner

def wish(name):
    print("hello",name,"god evening")
decorfunction=decor(wish)
decorfunction('sunny')
wish("sunny")
decorfunction('durga')
wish("digra")

def smartdivision(func):
    def inner(a,b):
        if b==0:
            print("hello stupid how we can divide woith zero")
            return
        else:
            return func(a,b)
    return inner
@smartdivision
def division(a,b):
     return a/b
print(division(10,2))
print(division(10,0))


def decor1(func):
    def inner(name):
        print("decor executed")
        func(name)
    return inner
def decor11(func):
    def inner(name):
        print("decor executedddds")
        func(name)
    return inner
@decor11
@decor1
def wish(name):
    print("hello",name,"good morning")
wish('durga')
