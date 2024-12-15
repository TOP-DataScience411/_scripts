class Test:
    
    def test1(param):
        print(param)
    
    def test2():
        print('функция без параметров в пространстве имён класса')


t1 = Test()

# >>> t1
# <__main__.Test object at 0x00000254A0FE8F50>
# >>> 
# >>> t1.test1()
# <__main__.Test object at 0x00000209B0E44410>
# >>> 
# >>> t1.test2()
# TypeError: Test.test2() takes 0 positional arguments but 1 was given


class Informer:
    
    @staticmethod
    def info():
        print('НОРМАЛЬНО')
    
    @staticmethod
    def warn():
        print('ТРЕВОЖНО')
    
    @staticmethod
    def critical():
        print('ОПАСНО')


# >>> from pprint import pprint
# >>>
# >>> pprint({
# ...   k: v
# ...   for k, v in Informer.__dict__.items()
# ...   if not k.startswith('__')
# ... })
# {'critical': <staticmethod(<function Informer.critical at 0x000001B0064F3CE0>)>,
#  'info': <staticmethod(<function Informer.info at 0x000001B0064F3BA0>)>,
#  'warn': <staticmethod(<function Informer.warn at 0x000001B0064F3C40>)>}


megafon = Informer()

# при вызове статического метода от экземпляра происходит подмена вызова без передачи экземпляра в качестве аргумента:
#   instance.stat_method -> <function Class.stat_method ...>
#   instance.stat_method(*args, **kwargs) -> Class.stat_method(*args, **kwargs)


# >>> Informer.info
# <function Informer.info at 0x000001B0064F3BA0>
# >>>
# >>> Informer.info()
# НОРМАЛЬНО
# >>>
# >>>
# >>> megafon.info
# <function Informer.info at 0x000001B0064F3BA0>
# >>>
# >>> megafon.info()
# НОРМАЛЬНО

