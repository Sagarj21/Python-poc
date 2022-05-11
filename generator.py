#generator
def mygen():
    yield 'a'
    yield 'b'

g=mygen()

for x in g:
    print(x)





#generate values oneby one dynamically
def countdown(num):
    print("Starrt conuntdown")
    while(num>0):
        yield num
        num=num-1
print(countdown(10))
values=countdown(10)
for x in values:
    print(x)