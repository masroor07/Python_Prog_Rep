#is an annonymous function with as many arguments but just a sole expression
def f1(n):
    return lambda a: a*n
doub= f1(2)
trip= f1(3)
print(doub(11))
print(trip(11))