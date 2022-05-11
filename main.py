import mymath
#import mymath as m
#mymath is user created file for module creation poc
print(mymath.x)
#print(m.x)
print(mymath.y)
mymath.add(10,20)
mymath.product(10,20)


import mymath as m
print(mymath.x)


#from import
from mymath import x,add
print(x)
print(add(10,20))

#another option to import as alising name
from mymath import x as a,y as b,add as c,product as d

"""variour possibilitiies of import
=================================
import modulename
import module1,module2,module3
import moddule1 as m
import module as m1,module as m2,module as module3


from module import member
from module import member1,member2,member3
from module import member1 as x
from module import *"""



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
