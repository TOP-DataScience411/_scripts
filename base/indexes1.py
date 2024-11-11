msg = 'Python — лучший язык программирования!'

# >>> len(msg)
# 38
# >>>
# >>> msg[0]
# 'P'
# >>> msg[1]
# 'y'
# >>> msg[len(msg)-1]
# '!'

fruits = ['яблоко', 'персик', 'груша', 'дыня', 'абрикос', 'слива']

# >>> type(fruits)
# <class 'list'>
# >>>
# >>> fruits[0]
# 'яблоко'
# >>>
# >>> fruits[3]
# 'дыня'

primes = (1, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29)

# >>> type(primes)
# <class 'tuple'>
# >>>
# >>> primes[0]
# 1
# >>> primes[1]
# 3
# >>> primes[5]
# 11


# >>> msg[50]
# IndexError: string index out of range
# >>>
# >>> fruits[9]
# IndexError: list index out of range
# >>>
# >>> primes[15]
# IndexError: tuple index out of range


# >>> msg[-1]
# '!'
# >>> msg[len(msg)-1]
# '!'
# >>> msg[-2]
# 'я'
# >>> msg[-len(msg)]
# 'P'

# >>> fruits[-1]
# 'слива'
# >>> primes[len(primes)-1]
# 29
# >>> fruits[-2]
# 'абрикос'
# >>> primes[len(primes)-2]
# 23
# >>> fruits[-len(fruits)]
# 'яблоко'

# >>> primes[-1]
# 29
# >>> primes[len(primes)-1]
# 29
# >>> primes[-2]
# 23
# >>> primes[-len(primes)]
# 1


# >>> fruits[5.5]
# TypeError: list indices must be integers or slices, not float
# >>>
# >>> fruits[5.5:6.6]
# TypeError: slice indices must be integers or None or have an __index__ method

