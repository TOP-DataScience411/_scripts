from numpy import array, ndarray, ones

from typing import Callable


class Neuron:
    """
    Реализация искусственного нейрона с динамическим количеством входов.
    """
    def __init__(
            self,
            activation_function: Callable,
            **activation_func_params
    ):
        # вызываемый объект функции активации
        self._non_linear = activation_function
        self._af_params = activation_func_params
        self.weights: ndarray = None
    
    def _linear(self, x: ndarray) -> float:
        if self.weights is None:
            self.weights = ones(x.shape)
        return (x * self.weights).sum()
    
    def out(self, x: ndarray) -> float:
        return self._non_linear(
            self._linear(x), 
            **self._af_params
        )


class DenseLayer(list):
    """
    Реализация полносвязного слоя нейронов.
    """
    def __init__(self, 
            n: int, 
            activation_function: Callable, 
            **activation_func_params
    ):
        for _ in range(n):
            self.append(Neuron(
                activation_function,
                **activation_func_params
            ))
    
    def out(self, x: ndarray) -> ndarray:
        return array([
            neuron.out(x)
            for neuron in self
        ])




