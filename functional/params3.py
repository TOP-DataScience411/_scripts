def line_length(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**.5


# >>> line_length(0, 0, 4, 0)
# 4.0
# >>>
# >>> line_length(0, y2=0, y1=0, x2=4)
# 4.0


def line_length(x1, y1, x2, y2, /):
    return ((x2 - x1)**2 + (y2 - y1)**2)**.5


# >>> line_length(0, 0, 4, 0)
# 4.0
# >>>
# >>> line_length(0, y2=0, y1=0, x2=4)
# TypeError: line_length() got some positional-only arguments passed as keyword arguments: 'y1, x2, y2'

