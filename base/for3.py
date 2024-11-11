prompt = 'введите число: '

n = 10
nums = []
auxiliary = range(n)
for _ in auxiliary:
    num = int(input(prompt))
    nums.append(num)

# >>> auxiliary
# range(0, 10)
# >>>
# >>> list(auxiliary)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>>
# >>> len(auxiliary)
# 10

# >>> nums
# [5, 10, 2, 46, 12, 29, 27, 2, 33, 18]
# >>>
# >>> nums[0]
# 5
# >>> type(nums[0])
# <class 'int'>

