class Test:
    pass


# >>> Test.__dict__.keys()
# dict_keys(['__module__', '__dict__', '__weakref__', '__doc__'])
# >>>
# >>> dir(Test)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# >>> Test.__mro__
# (<class '__main__.Test'>, <class 'object'>)


class A:
    attr1 = 10
    attr2 = 'abc'

class B(A):
    attr1 = 500

class C(A):
    pass

# >>> A.__mro__
# (<class '__main__.A'>, <class 'object'>)
# >>>
# >>> B.__mro__
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# >>>
# >>> C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# >>> {k: v for k, v in A.__dict__.items() if not k.startswith('__')}
# {'attr1': 10, 'attr2': 'abc'}
# >>>
# >>> {k: v for k, v in B.__dict__.items() if not k.startswith('__')}
# {'attr1': 500}
# >>>
# >>> {k: v for k, v in C.__dict__.items() if not k.startswith('__')}
# {}
# >>>
# >>> [k for k in dir(A) if not k.startswith('__')]
# ['attr1', 'attr2']
# >>>
# >>> [k for k in dir(B) if not k.startswith('__')]
# ['attr1', 'attr2']
# >>>
# >>> [k for k in dir(C) if not k.startswith('__')]
# ['attr1', 'attr2']

# >>> A.attr1
# 10
# >>> A.attr2
# 'abc'
# >>>
# >>> B.attr1
# 500
# >>> B.attr2
# 'abc'
# >>>
# >>> C.attr1
# 10
# >>> C.attr2
# 'abc'

# >>> b = B()
# >>> b.__dict__
# {}
# >>> b.attr1
# 500
# >>> b.attr2
# 'abc'
# >>>
# >>> c = C()
# >>> c.__dict__
# {}
# >>> c.attr1
# 10
# >>> C.attr2
# 'abc'

