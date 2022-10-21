from sandclock import sandclock


@sandclock(3, 6, 1)
def f1(x):
    print("f1: ", x)


f1("hello world")
