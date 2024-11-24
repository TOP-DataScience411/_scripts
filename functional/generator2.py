# range(1, 5) -> 1, 2, 3, 4
# range_doubled(1, 5) -> 1, 1, 2, 2, 3, 3, 4, 4


def range_doubled(start, stop):
    while start < stop:
        yield start
        yield start
        start += 1


rd = range_doubled(1, 5)

# >>> rd
# <generator object range_doubled at 0x000001DDBCC3F220>
# >>>
# >>> list(rd)
# [1, 1, 2, 2, 3, 3, 4, 4]
# >>>
# >>> list(rd)
# []

# >>> list(range_doubled(2, 6))
# [2, 2, 3, 3, 4, 4, 5, 5]
# >>>
# >>> list(range_doubled(2, 6))
# [2, 2, 3, 3, 4, 4, 5, 5]
# >>>

