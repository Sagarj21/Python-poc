
#bad approach    here  object wil be stored in memory
l=[x*x for x in range(100000000)]     #list compehrension
for x in l:
    print(x)




#Generator concept
#provides values on fly
#
#best approach  .here no object wil be stored in memory
l=(x*x for x in range(100000000))
for x in l:
    print(x)