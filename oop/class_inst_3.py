class Human:
    arms = 2
    legs = 2
    head = 1


igor = Human()
lena = Human()
ruslan = Human()

# >>> igor.arms
# 2
# >>> igor.__dict__
# {}
# >>>
# >>> lena.legs
# 2
# >>> lena.__dict__
# {}
# >>>
# >>> ruslan.head
# 1
# >>> ruslan.__dict__
# {}
# >>>
# >>> ruslan.legs = 1
# >>>
# >>> ruslan.__dict__
# {'legs': 1}
# >>>
# >>> ruslan.legs
# 1
# >>>
# >>> igor.legs
# 2
# >>> igor.__dict__
# {}
# >>>
# >>> Human.legs
# 2

