def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(3, 4, 5))


def fun(**kwargs):
    print(kwargs)
    print(kwargs["a"])

print(fun(a=1, b="Two", c=3))  #None 값을 반환한다.
