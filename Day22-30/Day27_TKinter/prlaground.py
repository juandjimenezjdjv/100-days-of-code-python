def add(*args):
    sum=0
    for n in (args):
        sum+=n
    return sum

#print(add(3,5,6))

# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n+=kwargs["add"]
#     n*=kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)
def test(*args):
    print((args))
 
test(1,2,3,5)
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)