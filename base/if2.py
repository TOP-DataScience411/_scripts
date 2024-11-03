# if выражение_1:
#     блок_1
# 
# elif выражение_2:
#     блок_2
# 
# ...
# 
# elif выражение_n:
#     блок_n
# 
# else:
#     блок_n+1


word = input('введите команду: ')

if word == 'line':
    print('—'*50)

elif word == 'square':
    print('—'*50)
    print(('|' + ' '*48 + '|\n')*5, end='')
    print('—'*50)

elif word == 'circle':
    print("! can't draw circle in terminal")

else:
    print('! unknown command')

print('end')

