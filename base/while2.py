prompt = 'введите имя: '

while True:
    name = input(prompt)
    if name.isalpha():
        break
    print('! вводите только буквы')

print(f'привет, {name}!')

