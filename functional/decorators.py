def decorator(function_object):
    print('начало вызова декоратора')
    
    def wrapper_function(*args, **kwargs):
        print('начало вызова обёртки')
        result = function_object(*args, **kwargs)
        print('конец вызова обёртки')
        return result
    
    print('конец вызова декоратора')
    return wrapper_function

