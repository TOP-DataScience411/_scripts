from pathlib import Path

scripts_dir = Path(r'd:\G-Doc\Scripts')

# >>> scripts_dir
# WindowsPath('d:/G-Doc/Scripts')
# >>> 
# >>> scripts_dir.parent
# WindowsPath('d:/G-Doc')

minst_archive = Path(r'dl\mnist.npz')

# >>> minst_archive
# WindowsPath('dl/mnist.npz')


cwd = Path.cwd()

# >>> type(cwd)
# <class 'pathlib.WindowsPath'>
# >>>
# >>> cwd
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/411/scripts/files')

from sys import path

current_file_dir = Path(path[0])

# >>> current_file_dir == cwd
# True


# >>> cwd
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/411/scripts/files')
# >>>
# >>> print(*cwd.parents, sep='\n')
# D:\G-Doc\TOP Academy\Data Science\411\scripts
# D:\G-Doc\TOP Academy\Data Science\411
# D:\G-Doc\TOP Academy\Data Science
# D:\G-Doc\TOP Academy
# D:\G-Doc
# D:\
# >>>
# >>> cwd.parents[3]
# WindowsPath('D:/G-Doc/TOP Academy')


test_file = cwd / 'test_file'

test_dir = cwd / 'test_dir'
test_dir.mkdir()

# >>> test_dir.mkdir()
# FileExistsError: [WinError 183] Невозможно создать файл, так как он уже существует: 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\files\\test_dir'
# >>> 
# >>> test_dir.mkdir(exist_ok=True)
# >>> 

test_file_2 = cwd / 'test_dir/1.txt'

# >>> test_file_2.is_file()
# False
# >>>
# >>> test_file_2.is_dir()
# False
# >>>
# >>> test_file_2.exists()
# False


print(*cwd.iterdir(), sep='\n')

# D:\G-Doc\TOP Academy\Data Science\411\scripts\files\path_construction.py
# D:\G-Doc\TOP Academy\Data Science\411\scripts\files\path_literals.py
# D:\G-Doc\TOP Academy\Data Science\411\scripts\files\test_dir
# D:\G-Doc\TOP Academy\Data Science\411\scripts\files\test_file

for p in cwd.iterdir():
  print(p.name)

# path_construction.py
# path_literals.py
# test_dir
# test_file

