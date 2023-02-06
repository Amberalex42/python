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


def func_interval(left, right):
    array = []
    temp = left
    while left < right:
        #print(f'[{f(left)}, {left}]')
        array.append([f(left), left])
        left += 0.01
    if array[0][0] > 0:
        print(f'f > 0 в промежутке {temp, right}')
        return max(array)
    elif array[0][0] < 0:
        print(f'f < 0 в промежутке {temp, right}')
        return min(array)


# 1. Определить корни
# funcrange = list(map(int, input("Задайте интервал фукнции через пробел: ").split()))
funcrange = [-7.7, 7.7]
leftnum = min(funcrange)
rightnum = max(funcrange)
roots = solution(leftnum, rightnum)

# 2. Найти интервалы, на которых функция возрастает, убывает, f > 0, f < 0 , координаты вершины
if len(roots) < 2:
    print("На заданном интервале нет вершин")
else:
    top = []
    for i in range(len(roots) - 1):
        top.append(func_interval(roots[i], roots[i + 1]))
    for j in top:
        j = [round(i, 2) for i in j]
        print(f'Координаты вершин функции: [{j[1]}, {j[0]}]')
    if len(top) < 2:
        print('error')
    else:
        for i in range(len(top) - 1):
            if top[i][0] > top[i + 1][0]:
                print(f'Функция убывает на интервале [{top[i][1]}, {top[i + 1][1]}]')
            else:
                print(f'Функция возрастает на интервале [{top[i][1]}, {top[i + 1][1]}]')

#3. Построить график функции
x = sympy.symbols('x')
plot(-12 * x ** 4 * sympy.sin(sympy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30, (x, leftnum, rightnum))
