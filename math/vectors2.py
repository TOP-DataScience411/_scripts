from numpy import array, dot


x_row = array([[1, 2, 3]])
x_col = x_row.T
x_flat = x_row.flatten()

y_row = array([[4, 5, 6]])
y_col = y_row.T
y_flat = y_col.flatten()

z = array([7, 8, 9])


# точечное (векторное) произведение

# >>> sum(x_flat[i] * y_flat[i] for i in range(len(x_flat)))
# np.int64(32)
# >>> 
# >>> dot(x_col.flat, y_col.flat)
# np.int64(32)
# >>> 
# >>> dot(x_row.flat, y_row.flat)
# np.int64(32)


# при передаче двуосных массивов в качестве аргументов функция dot() вычисляет матричное произведение

# в данном случае получаем внешнее произведение векторов
# >>> dot(x_col, y_row)
# array([[ 4,  5,  6],
#        [ 8, 10, 12],
#        [12, 15, 18]])

# в случаях ниже матричное произведение не определено — ошибка
# >>> dot(x_col, y_col)
# ValueError: shapes (3,1) and (3,1) not aligned: 1 (dim 1) != 3 (dim 0)
# >>> 
# >>> dot(x_row, y_row)
# ValueError: shapes (1,3) and (1,3) not aligned: 3 (dim 1) != 1 (dim 0)


# недопустимо передавать в качестве аргументов массивы с различным количеством осей

# >>> dot(x_col, z)
# ValueError: shapes (3,1) and (3,) not aligned: 1 (dim 1) != 3 (dim 0)

