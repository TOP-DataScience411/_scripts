num1 = input('введите число: ')
if num1.isdecimal():
    num1 = int(num1)
else:
    print('вводите только цифры')


num2 = input('введите число: ')
try:
    num2 = int(num2)
except ValueError:
    print('вводите только цифры')

