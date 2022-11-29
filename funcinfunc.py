def apply(func: object, value: object) -> object:
    return func(value)


# print(apply(id, 'strdad'))


def outer():
    def inner():
        print("This is inner.")


    print("This is outer, invoking inner.")
    return inner

def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k,v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k,v, sep='->', end=' ')
        print()

myfunc3()
myfunc3(1,2,3)
myfunc3(a=123, c=324)
myfunc3(123, 234, a=23)

# myfunc2(a=3, b=12)

# myfunc(10)
# myfunc()
# myfunc(10,20,30,40)
# myfunc(10, 'da', 32, '234', ['23','234'])

#
# i = outer()
# i()