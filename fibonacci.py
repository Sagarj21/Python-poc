# to generate fibonacci numbers:
#0,1,1,2,3,5,8........

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fib()
for x in f:
    if x>50:
        break
    print(x)