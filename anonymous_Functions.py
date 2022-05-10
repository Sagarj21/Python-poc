# function without name is anonymous functions
# it is just for instant use(only oem time use)
# lambda keyword is used
# ex s=lambda n:n*n
# syntax  lambda input:expression
from functools import reduce

s =lambda a,b:a if a>b else b
print("The biggest of {} and {} is : {}".format(2,4,s(2,4)))
print("The bieggets of {} and {} is : {}".format(20,40,s(20,40)))


# it is possible to pass the fuction as argument to other function

# filter()
#map()
#reduce()
print("----------------")
def iseven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l=[0,10,20,30,40,55,60]
l1=list(filter(lambda s: s%2==0,l)) #even filter
print(l1)
l2=list(filter(lambda s:s%2!=0,l)) # odd filter
print(l2)

print("********************")
#map()
#map(function,sequence)
def square(x):
    return x*x
l=[1,2,3,4,5]
#l1=list(map(square,l))
print(l1)

ll=[0,2,3,4]
l2=[10,20,30,40]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#functions
#sum of functions
#recursive function
#Anonymous functions=just for instant use
#lambda is a special keywords
s=lambda a:a*a
print(s(10))
l=[1,2,3,4,5,6,7,8,9,0,10,15,20]
l1=list(filter(lambda n:n%2!=0,l))
print(l1)
#filter input:10 output:<10

# map() function
# map() input:10 output:10
l=[0,1,2,3,4,5]
l1=list(map(lambda n:n*n,l))
print(l1)
#map(f,l)
l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)
# reduce() function
#reduce input=n number of values ,output= single value
#reduces squence of elements inot one by applying function
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y ,l)
print(result)

#difference between filter map reduce
#no of inputand output is same in map
# return tyoe is number
#filter returns a list
#
#
#





