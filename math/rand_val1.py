from numpy import array, sort


data = array([5, 7, 7, 8, 5, 6, 9, 6, 8, 5])

# X = array([5, 6, 7, 8, 9])
# X = data.unique()
X = []
for num in data:
    if num not in X:
        X.append(num)
X = sort(X)
# >>> X
# array([5, 6, 7, 8, 9])

W = {}
for num in data:
    W[num] = W.get(num, 0) + 1
W =  array(sorted(W.items())).T[1]
# >>> W
# array([3, 2, 2, 2, 1])

P = W / len(data)
# >>> P
# array([0.3, 0.2, 0.2, 0.2, 0.1])

M_X = sum(X * P).round(10)
# >>> M_X
# np.float64(6.6)


# >>> M_X == sum(data) / len(data) == data.mean()
# np.True_

