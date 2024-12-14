# при вызове объекта класса происходит подмена вызова:
#   Class(*args, **kwargs) -> Metaclass.__call__(Class, *args, **kwargs)


# примерный вид метода __call__() в метаклассе:
# class Metaclass:
#     def __call__(cls, *args, **kwargs):
#         instance = Metaclass.__new__(cls)
#         instance.__init__(*args, **kwargs)
#         return instance

