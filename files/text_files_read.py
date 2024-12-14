from pathlib import Path
from sys import path


script_dir = Path(path[0])
test_file = script_dir / 'test_file'
test_file_2 = script_dir / 'test_file_2.txt'


filein1 = open(test_file)

# >>> filein1.encoding
# 'cp65001'
# >>>
# >>> filein1.read()
# 'текстовый файл\nимя файла не содержит расширения\n'

filein2 = open(test_file, encoding='utf-8')

# >>> filein2.encoding
# 'utf-8'
# >>>
# >>> filein2.read()
# 'текстовый файл\nимя файла не содержит расширения\n'


filein3 = open(test_file_2)

# >>> filein3.encoding
# 'cp65001'
# >>>
# >>> filein3.read()
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd4 in position 0: invalid continuation byte

filein4 = open(test_file_2, encoding='koi8-r')

# >>> filein4.encoding
# 'koi8-r'
# >>> 
# >>> filein4.read()
# 'текст в другой кодировке\nпопробуй-ка это прочитать\nпрочитал?\nмолодец!\n'


test_2_lines = filein4.readlines()

# >>> test_2_lines
# ['текст в другой кодировке\n', 'попробуй-ка это прочитать\n', 'прочитал?\n', 'молодец!\n']

test_1_line1 = filein1.readline()

# >>> test_1_line1
# 'текстовый файл\n'

test_1_rest = filein1.read()

# >>> test_1_rest
# 'имя файла не содержит расширения\n'


filein1.close()
filein2.close()
filein3.close()
filein4.close()


with open(test_file_2, encoding='koi8-r') as filein5:
    line1 = filein5.readline()
    rest = filein5.read()

print(line1)
print(rest)


with open(test_file_2, encoding='koi8-r') as filein5:
    for line in filein5:
        print(line.strip())

