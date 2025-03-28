a = [1, 2, 3, 4]

# >>> id(a)
# 2668128686336
# >>>
# >>> a[0] = 10
# >>> a
# [10, 2, 3, 4]
# >>>
# >>> id(a)
# 2668128686336
# >>>
# >>> a[1:3]
# [2, 3]
# >>>
# >>> a[1:3] = [20, 30]
# >>> a
# [10, 20, 30, 4]
# >>>
# >>> id(a)
# 2668128686336
# >>>
# >>>
# >>> a.append([.6, .7])
# >>> a
# [10, 20, 30, 4, 5, [0.6, 0.7]]
# >>>
# >>> a.extend([8, 9])
# >>> a
# [10, 20, 30, 4, 5, [0.6, 0.7], 8, 9]



b = a.copy()

# >>> id(a)
# 2668128686336
# >>>
# >>> id(b)
# 2668130403776
# >>>
# >>> a == b
# True
# >>>
# >>> a is b
# False


c = a

# >>> id(a)
# 2668128686336
# >>>
# >>> id(c)
# 2668128686336
# >>>
# >>> a[0] = 1000
# >>> a
# [1000, 20, 30, 4, 5, [0.6, 0.7], 8, 9]
# >>>
# >>> c
# [1000, 20, 30, 4, 5, [0.6, 0.7], 8, 9]
# >>>
# >>> a == c
# True
# >>>
# >>> a is c
# True


# a.pop(-3)
# [0.6, 0.7]
# >>>
# >>> a
# [4, 5, 20, 30, 1000, 8, 9]
# >>>
# >>> a.sort()
# >>> a
# [4, 5, 8, 9, 20, 30, 1000]
# >>>
# >>> id(a)
# 2668128686336

