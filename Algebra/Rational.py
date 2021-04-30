
from .Natural import *
from .Integer import *

__all__ = ["Rational"]

class Rational():

    # _numerator - числитель рационального числа
    # _denumerator - знаменатель рационального числа
    def __init__(self, n: str = None):
        if not n:
            self._numerator = Integer("0")
            self._denumerator = Natural("0")
        elif not Rational.isRational(n):
            raise Exception("number passed to \"Rational\" class constructor is invailid")
        else:
            k = n.find("/")
            if k == -1:
                self._numerator = Integer(n)
                self._denumerator = Natural("1" if self._numerator != Integer("0") else "0")
            else:
                num = n[:k]
                denum = n[k + 1:]
                self._numerator = Integer(num)
                self._denumerator = Natural(denum)
                if self._numerator == Integer("0"):
                    self._numerator = Integer("0")
                    self._denumerator = Natural("0")

    def __gt__(self, num):
        res = self - num
        if res._numerator._sign == POSITIVE:
            return True
        else:
            return False

    def is_zero(self):
        return self._numerator.is_zero()

    @staticmethod
    def isRational(s):
        k = s.find("/")
        if k == -1:
            return Integer.isInteger(s)
        else:
            integerPart, naturalPart = s[:k], s[k + 1:]
            integer, natural = Integer(integerPart), Natural(naturalPart)
            if natural.is_zero() and not integer._number.is_zero():
                return False
            return Integer.isInteger(integerPart) and Natural.isNatural(naturalPart)

    def __str__(self):
        return str(self._numerator) + "/" + str(self._denumerator)

    '''МОДУЛИ RATIONAL'''

    def reduce(self):
        '''Модуль Q-1 RED_Q_Q. Выполнил и оформил Шабров Иван'''

        if self.is_zero():
            return Rational("0/0")

        r = Rational()
        # Вычисляем НОД числителя и знаменателя
        gcf = abs(self._numerator).gcf(self._denumerator)
        # Переводим k из Natural в Integer
        gcf_int = Integer.natural_to_integer(gcf)

        r._denumerator = self._denumerator / gcf
        r._numerator = self._numerator / gcf_int

        return r

    def is_int(self):
        '''Модуль Q-2 INT_Q_B. Выполнил и оформил Щусь Максим'''

        num = self.reduce()
        return num._denumerator == Natural("1") or num.is_zero()

    @staticmethod
    def integer_to_rational(integer):
        '''Модуль Q-3 TRANS_Z_Q. Выполнил и оформил Трибунский Алексей'''

        # Числитель равен введенному числу, знаменатель равен единице
        res = Rational()
        res._numerator = Integer(str(integer))
        res._denumerator = Natural("1")
        return res

    @staticmethod
    def to_integer(rational):
        '''Модуль Q-4 TRANS_Q_Z. Выполнила и оформила Показацкая Арина'''

        # Если знаменатель равен "1", число преобразуется в целое
        rational = rational.reduce()
        if rational.is_int():
            return Integer(str(rational._numerator))
        else:
            raise Exception("unable to convert rational number into integer (denumerator is not equal to 1)")

    def __add__(self, num):
        '''Модуль Q-5 ADD_QQ_Q. Выполнил и оформил Проскуряк Влад'''

        if self.is_zero():
            return Rational(str(num))
        elif num.is_zero():
            return Rational(str(self))

        # lcm - знаменатель искомой дроби
        res = Rational(str(self))
        lcm = self._denumerator.lcm(num._denumerator)

        # Получаем числитель первой дроби
        common_div1 = Integer(str(lcm / res._denumerator))
        num1 = res._numerator * common_div1

        # Получаем числитель второй дроби
        common_div2 = Integer(str(lcm / num._denumerator))
        num2 = num._numerator * common_div2

        res._numerator = num1 + num2
        res._denumerator = lcm

        return res

    def __sub__(self, num):
        '''Модуль Q-6 SUB_QQ_Q. Выполнил и оформил Цыганков Дмитрий'''

        # Проверка на ноль
        if self.is_zero():
            res = Rational(str(num))
            res._numerator.change_sign()
            return res
        elif num.is_zero():
            return Rational(str(self))

        res = Rational()
        # Общий знаминатель
        denum = self._denumerator.lcm(num._denumerator)
        res._denumerator = denum
        # Вычесление числителя
        res._numerator = self._numerator * Integer(str(denum / self._denumerator)) - num._numerator * Integer(str(denum / num._denumerator))
        return res

    def __mul__(self, num):
        '''Модуль Q-7 MUL_QQ_Q. Выполнил и оформил Жексенгалиев Адиль'''

        # Проверка на ноль
        if self.is_zero() or num.is_zero():
            return Rational("0")

        res = Rational()
        res._numerator = self._numerator * num._numerator
        res._denumerator = self._denumerator * num._denumerator

        return res

    def __truediv__(self, num):
        '''Модуль Q-8 DIV_QQ_Q. Выполнила и оформила Реброва Юлия'''

        # Проверка на ноль
        if num.is_zero():
            raise Exception("unable to divide by zero")
        elif self.is_zero():
            return Rational("0/0")

        res = Rational()
        # "Переворачиваем" дробь
        n = Integer.natural_to_integer(num._denumerator)
        m = abs(num._numerator)
        res._numerator = self._numerator * n
        res._denumerator = self._denumerator * m

        return res