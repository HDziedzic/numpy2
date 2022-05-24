# Numpy 2 ćwiczenia
import math
import numpy as np


def zad1():
    a = np.arange(3).reshape(1, 3)
    b = np.arange(4, 7).reshape(1, 3)
    print(a * b.T)


def zad2():
    a = np.linspace(0, 10, 9, dtype='int32').reshape(3, 3)
    b = np.linspace(0, 100, 16, dtype='int32').reshape(4, 4)
    print('a', a, '\n-------------')
    print('b', b)
    print('minimum każdego rzędu')
    print('a', a.min(axis=1))
    print('b', b.min(axis=1))
    print('minimum każdej kolumny')
    print('a', a.min(axis=0))
    print('b', b.min(axis=0))


def zad3():
    a = np.arange(3).reshape(1, 3)
    b = np.arange(4, 7).reshape(1, 3)
    result = np.dot(a.T, b)
    print(result)


def zad4():
    a = np.linspace(1, 3, 3, dtype='int32').reshape(1, 3)
    b = np.linspace(-1, 2, 3).reshape(1, 3).reshape(1, 3)
    print(a * b)


def zad5():
    matrix = np.arange(1, 7).reshape(2, 3)
    a = np.zeros(6)
    i = 0
    for b in matrix.flat:
        float(b)
        a[i] = math.sin(b)
        i += 1
    a = a.reshape(2, 3)
    return a


def zad6():
    matrix = np.arange(1, 7).reshape(2, 3)
    b = np.zeros(6)
    i = 0
    for c in matrix.flat:
        float(c)
        b[i] = math.cos(c)
        i += 1
    b = b.reshape(2, 3)
    return b


def zad7():
    a = zad5()
    b = zad6()
    print(a + b)


def zad8():
    a = np.arange(9).reshape(3, 3)
    for b in a:
        print(b)
        print('')


def zad9():
    a = np.logspace(2, 5, 9, base=3).reshape(3, 3)
    for b in a.flat:
        print('{b:.2f}'.format(b=b))


def zad10():
    a = np.arange(81).reshape(9, 9)
    print(a.reshape(1, 81))
    print(a.reshape(3, 27))
    print(a.reshape(9, 9))
    print(a.reshape(3, 3, 3, 3))
    print(a.reshape(9, 3, 3))


def zad11():
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(a)
    a = a.reshape(3, 4)
    b = a.reshape(4, 3)
    c = a.reshape(2, 6)
    print(a.flat)
    print(b.flat)
    print(c.flat)


zad11()
