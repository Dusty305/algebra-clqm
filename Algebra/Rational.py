
from .Integer import *
from .Natural import *

__all__ = ["Rational"]

class Rational():

    def __init__(self, n, m):
        self._numerator = Integer(n)
        self._denumerator = Natural(m)

    def __str__(self):
        return str(self._numerator) + " / " + str(self._denumerator)

    def to_integer(self, n, m):
        ''' Функция преобразования дробного числа в целое '''
    # Показацкая Арина
        self._numerator = n
        self._denumerator = m
        if self._denumerator == "1":
            return self._numerator
