from random import randrange
from time import perf_counter


start = perf_counter()

nums = [randrange(10) for _ in range(10**6)]

end = perf_counter()

print(f'{end - start = :.3f} с')

