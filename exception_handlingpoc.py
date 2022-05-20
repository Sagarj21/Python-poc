print('stmt 1')
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print('stmt 2')
#isnted ZeroDivisionError we can use baseException
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("exception occured is: ",msg)

""""""

#single excepton block that can handle multiple exceptions
#default except block ALSO CAN BE WRITTEN
#DEFAULT EXCEPT BLOCK SHOULD BE at LAST
try:
    x=int(input("enter dfirst number"))
    y=int(input("enetr first  number"))
    print(x/y)
except (ZeroDivisionError,ValueError)as msg:
    print("plz provide valid number onoly",msg)

#finally
try:
    print("try")
    print(10/0)
except ValueError:
    print("exception")
finally:
    print("finally")



#comtrol flow in try except and finally block
try:
    stmt1
    stmt2
    stmt3
except xyz:
    stmt4
finally:
    stmt 5
stmt 6

no exception       1 2 3 5 6   NT
exceptioon at 2 except vailable     1 4 5 6  NT
exception at 2   except not vailable    1  5  AT
exception at 4       1 2 3  5 AT
exception at 5   AT
exception at 6   AT
