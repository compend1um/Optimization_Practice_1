from methods import method2
from calls.bessel_functions import *


def call_j0():
    print(method2.iteration(func_j_0, -0.01, 2, 10 ** (-10)))
    print(method2.iteration(func_j_0, 0.01, 4, 10 ** (-10)))

def call_j1():
    print(method2.iteration(func_j_1, 0.01, 3.2, 10 ** (-10)))
    print(method2.iteration(func_j_1, 0.01, 7, 10 ** (-10)))

def call_y0():
    print(method2.iteration(func_y_0, 0.01, 3.2, 10 ** (-10)))
    print(method2.iteration(func_y_0, 0.01, 7, 10 ** (-10)))

def call_y1():
    print(method2.iteration(func_y_1, 0.01, 2, 10 ** (-10)))
    print(method2.iteration(func_y_1, 0.01, 5.5, 10 ** (-10)))


def print_():
    print("===== метод простой итерации =====")

    print("корни j0")
    call_j0()

    print("\nкорни j1")
    call_j1()

    print("\nкорни y0")
    call_y0()

    print("\nкорни y1")
    call_y1()

    return None

