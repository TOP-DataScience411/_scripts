class Proteus:
    @staticmethod
    def move():
        print('движение')
    
    @staticmethod
    def eat():
        print('еда')
    
    @staticmethod
    def reproduce():
        print('размножение')


class Fish(Proteus):
    @staticmethod
    def breath():
        print('дыхание')


class Reptile(Fish):
    @staticmethod
    def hide():
        print('скрытность')


class Bird(Reptile):
    @staticmethod
    def fly():
        print('полёт')


class Mammal(Reptile):
    @staticmethod
    def care():
        print('забота')


class Human(Mammal):
    @staticmethod
    def speak():
        print('речь')


kolya = Human()
kesha = Bird()

# >>> [k for k in dir(kolya) if not k.startswith('__')]
# ['breath', 'care', 'eat', 'hide', 'move', 'reproduce', 'speak']
# >>>
# >>> print(*kolya.__class__.__mro__, sep='\n')
# <class '__main__.Human'>
# <class '__main__.Mammal'>
# <class '__main__.Reptile'>
# <class '__main__.Fish'>
# <class '__main__.Proteus'>
# <class 'object'>

# >>> [k for k in dir(kesha) if not k.startswith('__')]
# ['breath', 'eat', 'fly', 'hide', 'move', 'reproduce']
# >>>
# >>> print(*kesha.__class__.__mro__, sep='\n')
# <class '__main__.Bird'>
# <class '__main__.Reptile'>
# <class '__main__.Fish'>
# <class '__main__.Proteus'>
# <class 'object'>

