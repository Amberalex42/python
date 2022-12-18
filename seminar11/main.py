# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
#
#     Определить корни
#
#     Найти интервалы, на которых функция возрастает
#
#     Найти интервалы, на которых функция убывает
#
#     Построить график
#
#     Вычислить вершину
#
#     Определить промежутки, на котором f > 0
#
#     Определить промежутки, на котором f < 0

import sympy
from sympy.plotting import plot
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy


def f(x):
    return -12 * x ** 4 * numpy.sin(numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


def solution(leftnum, rightnum):
    temp = leftnum
    roots = []
    while temp < rightnum:
        if f(temp) >= 0 and f(temp + 1) <= 0:
            w = fsolve(f, temp)
            roots.append(*w)
        elif f(temp) <= 0 and f(temp + 1) >= 0:
            pass
            roots.append(*fsolve(f, temp))
        temp += 1
    roots = [round(i, 2) for i in roots]
    print(f'Корни уравнения для заданного интервала: {roots}')
    return roots


# 1. Определить корни
# funcrange = list(map(int, input("Задайте интервал фукнции через пробел: ").split()))
funcrange = [-10, 10]
leftnum = min(funcrange)
rightnum = max(funcrange)
roots = solution(leftnum, rightnum)

# 2. Найти интервалы, на которых функция возрастает