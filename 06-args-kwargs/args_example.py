
def total(*args):
    t = 0
    for arg in args:
        t += arg
    return t


def test_parameters(**kwargs):
    for key in kwargs:
        print(key, ' = ', kwargs[key])


def test_all(w, h, *args, **kwargs):
    print("w=", w)
    print("h=", h)
    print(len(args))
    print(len(kwargs))


# print(total(1, 3, 5, 8, 9))
# print(total(3, 6, 10))
# print(total(5))
#
# test_parameters(name="John", last_name="Doe", age=56)

test_all(45, 23)
test_all(45, 23, 1, 2, 3, 4, 5, 6)
test_all(45, 23, 1, 2, 3, 4, 5, 6, shape="Square", color="blue")
test_all(45, 23, shape="Square", color="blue")
