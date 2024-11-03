# try:
#     блок_с_потенциальной_ошибкой
# 
# except ValueError:
#     блок_при_перехвате_ValueError
# 
# except IndexError as exception_object:
#     блок_при_перехвате_IndexError_с_объектом_исключения
# 
# except (TypeError, AttributeError):
#     блок_при_перехвате_TypeError_или_AttributeError
# 
# ...
# 
# except:
#     блок_при_перехвате_любого_другого_исключения
# 
# else:
#     блок_при_отсутствии_исключения
# 
# finally:
#     блок_выполняющийся_всегда


# try - except
# try - except - else
# try - except - finally
# try - except - else - finally
# try - finally


try:
    4 / 0

except ZeroDivisionError:
    print('перехвачено исключение для ошибки деления на ноль')

print("конец программы")

