def f():
    def a():
        print('Hello')
    return a


def c(func):
    print(id(func))


b = f()
c(b)
print(id(b))