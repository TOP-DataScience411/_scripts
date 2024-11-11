def test_func1():
    a, b = 5, 8
    return a + b


def test_func2():
    a, b = 5, 8
    print(a + b)


test_func1()
test_func2()

var1 = test_func1()
var2 = test_func2()

# >>> var1
# 13
# >>> type(var1)
# <class 'int'>
# >>>
# >>> var2
# >>>
# >>> type(var2)
# <class 'NoneType'>
# >>>
# >>> print(var2)
# None


# >>> test_func1()
# 13
# >>> a = test_func1()
# >>> a
# 13
# >>>
# >>> test_func2()
# 13
# >>> b = test_func2()
# 13
# >>> b
# >>> type(b)
# <class 'NoneType'>


def test_func3():
    return


# >>> test_func3()
# >>>
# >>> var3 = test_func3()
# >>> var3
# >>>
# >>> type(var3)
# <class 'NoneType'>


