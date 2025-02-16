from numpy import arange, array
from numpy.linalg import inv


matr1 = arange(1, 10).reshape(3, 3)
matr2 = array([
    [1, 4],
    [2, 7],
])


# псевдообратная матрица
# >>> inv(matr1)
# array([[-4.50359963e+15,  9.00719925e+15, -4.50359963e+15],
#        [ 9.00719925e+15, -1.80143985e+16,  9.00719925e+15],
#        [-4.50359963e+15,  9.00719925e+15, -4.50359963e+15]])
# >>>
# >>>
# >>> matr1 @ inv(matr1)
# array([[ 0.,  0.,  0.],
#        [-4.,  0.,  4.],
#        [ 0.,  0.,  8.]])
# >>>
# >>> inv(matr1) @ matr1
# array([[ 12.,   8.,   8.],
#        [-16.,  -8.,   0.],
#        [  4.,   0.,   0.]])


# (полная) обратная матрица
# >>> inv(matr2)
# array([[-7.,  4.],
#        [ 2., -1.]])
# >>>
# >>>
# >>> matr2 @ inv(matr2)
# array([[1., 0.],
#        [0., 1.]])
# >>>
# >>> inv(matr2) @ matr2
# array([[1., 0.],
#        [0., 1.]])


from matplotlib import pyplot as plt
from PIL import Image

from pathlib import Path
from sys import path 


img = Image.open(Path(path[0]) / 'code_white_1.ico')
img = array(img.getchannel(0))


fig = plt.figure(figsize=(12, 6))
axs = fig.subplots(1, 2)

axs[0].imshow(img, cmap='gray')

# не существует полной обратной матрицы для рангово-пониженной (сингулярной)
# axs[1].imshow(inv(img))

# инвертированное изображение — это НЕ обратная матрица
axs[1].imshow(255 - img, cmap='gray')

fig.show()

