
from calls.bessel_functions import *
from methods import method1


#метод деления отрезка пополам

def call_j0():
    print(method1.find_(0, 5, func_j_0, 10 ** (-10)))
    print(method1.find_(5, 7.5, func_j_0, 10 ** (-10)))

def call_j1():
    print(method1.find_(0, 5, func_j_1, 10 ** (-10)))
    print(method1.find_(5, 7.5, func_j_1, 10 ** (-10)))

def call_y0():
    print(method1.find_(0, 5, func_y_0, 10 ** (-10)))
    print(method1.find_(5, 7.5, func_y_0, 10 ** (-10)))

def call_y1():
    print(method1.find_(0, 5, func_y_1, 10 ** (-10)))
    print(method1.find_(5, 7.5, func_y_1, 10 ** (-10)))


def print_():
    print("===== метод деления отрезка пополам =====")

    print("корни j0")
    call_j0()

    print("\nкорни j1")
    call_j1()

    print("\nкорни y0")
    call_y0()

    print("\nкорни y1")
    call_y1()

    return None


