class Neuron:
    """
    Реализация искусственного нейрона с фиксированным количеством входов и фиксированной функцией активации.
    """
    def __init__(self, weight1=1, weight2=1):
        self.w1 = weight1
        self.w2 = weight2
    
    def _linear(self, x1, x2):
        """Линейное преобразование — сумматор."""
        return x1*self.w1 + x2*self.w2
    
    def _non_linear(self, x, cutoff=0):
        """Нелинейное преобразование — ступенчатая функция (Хэвисайда)."""
        if x < cutoff:
            return 0
        else:
            return 1
    
    def out(self, x1, x2):
        return self._non_linear(self._linear(x1, x2))


if __name__ == '__main__':
    
    temperature_1 = (9, 10)
    temperature_2 = (10, 16)
    temperature_3 = (16, 8)
    
    # подбор весов
    weather = Neuron(-1, 1)
    
    print(
        weather.out(*temperature_1),
        weather.out(*temperature_2),
        weather.out(*temperature_3),
    )

