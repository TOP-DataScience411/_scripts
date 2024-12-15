class Square:
    def __init__(self, side):
        self.__side = float(side)
        self.__area = float(side ** 2)
    
    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, new_side):
        self.__side = float(new_side)
        self.__area = float(new_side ** 2)
    
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, new_area):
        self.__side = new_area ** 0.5
        self.__area = float(new_area)


sq1 = Square(5)


# до добавления свойств
# >>> sq1.side
# 5.0
# >>> sq1.area
# 25.0
# >>>
# >>> sq1.side = 10
# >>> sq1.side
# 10.0
# >>> sq1.area
# 25.0
# >>>
# >>> sq1.area = 80
# >>> sq1.area
# 80.0
# >>> sq1.side
# 10.0


# после добавления свойств
# >> sq1.side
# 5.0
# >>> sq1.area
# 25.0
# >>>
# >>> sq1.side = 10
# >>> sq1.side
# 10.0
# >>> sq1.area
# 100.0
# >>>
# >>> sq1.area = 49
# >>> sq1.area
# 49.0
# >>> sq1.side
# 7.0

