from sys import path

for p in path:
    print(p)

# D:\G-Doc\TOP Academy\Data Science\411\scripts\namespaces
# C:\Python312\python312.zip
# C:\Python312\DLLs
# C:\Python312\Lib
# C:\Python312
# C:\Python312\Lib\site-packages

path.insert(1, r'd:\G-Doc\TOP Academy\Data Science\411\scripts\functional')

for p in path:
    print(p)

# D:\G-Doc\TOP Academy\Data Science\411\scripts\namespaces
# d:\G-Doc\TOP Academy\Data Science\411\scripts\functional
# C:\Python312\python312.zip
# C:\Python312\DLLs
# C:\Python312\Lib
# C:\Python312
# C:\Python312\Lib\site-packages

import funcs3

