

#function inside function == to definefunction specific repeatedly rewuired fujkctionality
#you cant call this function oyreride the outer fucntion


def f1():
    def inner(a,b):
        print("t8he sum",a+b)
        print("the avg",(a+b)/2)
    inner(10,20)
    inner(100,200)
f1()


#function as argumemmt to anotthrt function
#filter function


#a fucnytiom can return another function
def outer():
    print("Outer function started")
    def inner():
        print("inner funcytion execution")
    print("outer function frertirnaing inner funcyipom")
    return inner()
f1=outer()  #this is nothing but function aliasing
print(f1)
print(id(f1))
print(type(f1))


