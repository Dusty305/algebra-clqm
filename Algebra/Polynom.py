
from .Natural import *
from .Integer import *
from .Rational import *

__all__ = ["Polynom"]

class Polynom():

    # _coef - массив коэффициентов начиная с меньшего и заканчивая большим
    # _coef_n - количество коэффициентов
    def __init__(self, l: list = None):
        if not l:
            self._coef = [Rational("0")]
            self._coef_n = 1
        else:
            try:
                self._coef = [Rational(str(i)) for i in l[::-1]]
                self._coef_n = len(l)
            except:
                raise Exception("error while converting coefficients into rational numbers")

    # TO DO:
    # Пофиксить вывод отрицательных коэффициентов
    def __str__(self):
        i = self._coef_n
        while self._coef[i - 1]._numerator._number.is_zero() and i > 1:
            i -= 1
        return " ".join(map(str, self._coef[i - 1::-1]))

    def is_zero(self):
        return self.power() == 0 and self._coef[0].is_zero()

    def __gt__(self, num):
        '''Перегрузка > для класса Polynom. Выполнил Шабров Иван'''
        if self.power() > num.power():
            return True
        elif self.power() < num.power():
            return False
        else:
            for i in range(self.power(), -1, -1):
                if self._coef[i] > num._coef[i]:
                    return True
                else:
                    return False

    '''МОДУЛИ POLYNOM'''

    def __add__(self, pol):
        '''Модуль P-1 ADD_PP_P. Выполнил и оформил Щусь Максим'''

        # Если степень p2 больше p1
        if pol._coef_n > self._coef_n:
            res = Polynom(pol._coef[::-1])
            # Складываем коэффициенты соответствующих степеней
            for i in range(self._coef_n):
                res._coef[i] = res._coef[i] + self._coef[i]
        # Если степень p2 не меньше p1
        else:
            res = Polynom(self._coef[::-1])
            # Складываем коэффициенты соответствующих степеней
            for i in range(pol._coef_n):
                res._coef[i] = res._coef[i] + pol._coef[i]

        return res

    def __sub__(self, num):
        '''Модуль P-2 SUB_QQ_Q. Выполнила и оформила Показацкая Арина'''

        # Cтепень большего многочлена
        k = max(self.power(), num.power())
        # Степень меньшего многочлена
        c = min(self.power(), num.power())

        res = Polynom([Rational("0") for i in range(k + 1)])

        # Если количество коэффициентов первого больше(или равно) второго
        if self._coef_n >= num._coef_n:
            for i in range(k + 1):
                # Записываем в результат первый многочлен и вычитаем из него второй
                res._coef[i] = Rational(str(self._coef[i]))
            for i in range(c + 1):
                res._coef[i] = res._coef[i] - num._coef[i]
        # Если количество коэффициентов второго больше первого
        else:
            # Записываем в результат второй многочлен и вычитаем из него первый
            for i in range(k + 1):
                res._coef[i] = Rational(str(num._coef[i]))
            for i in range(c + 1):
                res._coef[i] = self._coef[i] - res._coef[i]
            # Вычитаем нулевые коэффициенты
            zero = Rational("0")
            for i in range(c + 1, k + 1):
                res._coef[i] = zero - res._coef[i]

        # Удаляем старшие нулевые коэффициенты, если такие есть
        while (res._coef[res._coef_n - 1] == 0):
            res._coef.pop()
            res._coef_n -= 1

        return res

    def mul_q(self, num):
        '''Модуль P-3 MUL_PQ_P. Выполнил и оформил Жексенгалиев Адиль'''

        # Проверка на ноль
        if self.is_zero() or num.is_zero():
            return Polynom([0])

        res = Polynom()
        res._coef_n = self._coef_n
        res._coef = [Rational("1") for i in range(res._coef_n)]

        # Поочередно перемножаем коэффициенты на num
        for i in range(self._coef_n):
            res._coef[i] = self._coef[i] * num

        return res

    def mul_xk(self, k: int):
        '''Модуль P-4 MUL_Pxk_P. Выполнила и оформила Реброва Юлия'''

        if k < 0:
            raise Exception("unable to multiple polynom by x^k when k is negative")
        # Степень результирующего полинома увеличивается на k
        res = Polynom(["0"] * (self._coef_n + k))
        # Увеличиваем степени "иксов" изначального полинома
        for i in range(self._coef_n):
            res._coef[i + k] = self._coef[i]
        return res

    def higher_coef(self):
        '''Модуль P-5 LED_P_Q. Выполнил и оформил Шабров Иван'''

        return self._coef[-1]

    def power(self):
        '''Модуль P-6 DEG_P_N. Выполнил и оформил Солодков Никита'''

        # Степень многочлена на единицу меньше количества коэффициентов
        # (нули при старших коэффициентах не считаются)
        i = 0
        while (i + 1) < self._coef_n and self._coef[-i - 1].is_zero():
            i += 1
        return self._coef_n - i - 1

    def fac(self):
        '''Модуль P-7 FAC_P_Q. Выполнил и оформил Солодков Никита'''

        res = Rational()
        # Присваиваем НОД и НОК значение числителя и знаменателя первых элементов соответственно
        num_gcf = abs(self._coef[0]._numerator)
        num_lcm = self._coef[0]._denumerator
        # Циклом проходим по всем коэффициентам многочлена
        for i in range(1, self._coef_n):
            # Если хотя бы один коэффициент не равен 0
            if not (self._coef[i].is_zero() and num_gcf.is_zero()):
                num_gcf = num_gcf.gcf(abs(self._coef[i]._numerator))
            # Если оба коэффициента не равны 0
            if not (self._coef[i].is_zero() or num_lcm.is_zero()):
                num_lcm = num_lcm.lcm(self._coef[i]._denumerator)
            # Если i-тый коэффициент не равен 0
            elif num_lcm.is_zero() and not self._coef[i].is_zero():
                num_lcm = self._coef[i]._denumerator

        res._numerator = Integer.natural_to_integer(num_gcf)
        res._denumerator = Natural(str(num_lcm))

        return res

    def __mul__(self, p):
        '''Модуль P-8 MUL_PP_P. Выполнил и оформил Трибунский Алексей'''

        # Проверка на 0
        if self.is_zero() or p.is_zero():
            return Polynom([0])

        res = Polynom([0])
        # Умножаем self на i-тый коэффициент второго полинома
        # и возводим в степень i
        for i in range(p._coef_n):
            res += self.mul_q(p._coef[i]).mul_xk(i)
        return res

    def __truediv__(self, pol):
        '''Модуль P-9 DIV_PP_P. Выполнил и оформил Цыганков Дмитрий'''

        divisbl = Polynom(self._coef[::-1])
        pol_ = Polynom(pol._coef[::-1])

        # Уберем нули при старших степенях в pol
        while pol_._coef[-1].is_zero():
            pol_._coef.pop(-1)
            pol_._coef_n -= 1

        # Проверка на ноль
        if pol_.is_zero():
            raise Exception("unable to divide polynom by zero")
        elif divisbl.is_zero() or divisbl.power() < pol_.power():
            return Polynom()

        # степнь искомого полинома
        deg = divisbl.power() - pol_.power() + 1
        result = Polynom([0] * deg)
        i = 0
        while divisbl.power() >= pol_.power():
            # Вычисляем очередной коэффициент частного
            res_coef = divisbl._coef[-1] / pol_._coef[-1]
            result._coef[deg - i - 1] = res_coef
            # Умножаем делитель на полученный коэффициент res_coef
            temp_pol = pol_.mul_q(res_coef)
            # Вычитаем temp_pol из делимого
            temp_pol = temp_pol.mul_xk(divisbl._coef_n - pol_._coef_n)
            divisbl -= temp_pol
            # Удаляем старший нулевой коэффициент
            divisbl._coef.pop(-1)
            divisbl._coef_n -= 1
            i += 1

        return result

    def __mod__(self, num):
        '''Модуль P-10 MOD_PP_P. Выполнил и оформил Проскуряк Влад'''

        if num.is_zero():
            raise Exception("unable to find modulo by zero")
        res = Polynom(self._coef[::-1])
        resnum = Polynom(num._coef[::-1])
        # Вычитаем из многочлена произведение второго многочлена на частное от деления многочленов и получаем остаток
        res = res - resnum * (res / resnum)
        return res

    def gcf(self, num):
        '''Модуль P-11 GCF_PP_P. Выполнил и оформил Шабров Иван'''

        # Проверка на ноль
        if self.is_zero() and num.is_zero():
            raise Exception("gcf of both zeros is undefined")
        a = Polynom(self._coef[::-1])
        b = Polynom(num._coef[::-1])

        if b > a:
            a, b = b, a

        while b.power() != 0:
            temp = b
            a, b = b, a % b
            if b.is_zero():
                b = temp
                break

        if b.power() == 0 and not b._coef[0].is_int():
            return Polynom([1])
        return b

        # while not a.is_zero() and not b.is_zero():
        #     if a > b:
        #         a = a % b
        #     else:
        #         b = b % a
        #     print(a.power(), b.power())
        #     print(a)
        #     print(b)
        #
        # res = b if a.is_zero() else a
        # if res.power() == 0 and not res._coef[0].is_int():
        #     res = Polynom([1])
        # return res

    def derivate(self):
        '''Модуль P-12 DER_P_P. Выполнил и оформил Щусь Максим'''

        if self.power() == 0:
            return Polynom([0])
        res = Polynom(self._coef[::-1])
        # Диффиренцируем каждый элемент полинома
        for i in range(self.power()):
            res._coef[i] = self._coef[i + 1] * Rational(str(i + 1))
        # Убираем последний "лишний" элемент
        res._coef.pop(-1)
        res._coef_n -= 1

        return res

    def nmr(self):
        '''Модуль P-13 NMR_P_P. Выполнил и оформил Цыганков Дмитрий'''

        pol_ = Polynom(self._coef[::-1])
        if pol_.is_zero():
            return pol_
        # Делим полином на НОД от него и его производной
        pol_ /= pol_.gcf(pol_.derivate())
        return pol_