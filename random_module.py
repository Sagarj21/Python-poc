from random import *
#help(random)
#random()
for i in range(10):
    print(random())


#randint(start,end)    inclusive
for i in range(10):
    print(randint(1,5))

#uniform()        exclusive
for i in range(10):
    print(uniform(1,10))

#randrange(strt,stop,step)   start<=step<stop
for i in range(5):
    print(randrange(5))
    print(randrange(1, 7))
    print(randrange(1,7,2))

#choice()It wont return random number.It will return a random object from the given list or tuple.
l=['sunny','chinny','bunny','lunny','kinny']
for i in range(5):
    print(choice(l))
for i in range(5):
    print(choice('sagar'))


