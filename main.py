import numpy, scipy, matplotlib
from methods import method1
from methods import method2


# метод 1

func_j_0 = lambda x: scipy.special.jv(0, x)
func_j_1 = lambda x: scipy.special.jv(1, x)
func_v_0 = lambda x: scipy.special.yv(0, x)
func_v_1 = lambda x: scipy.special.yv(1, x)

# пример печати, надо еще три таких же
#print(method1.find_(0, 5, func_j_0, 10 ** (-10)))


# method 2, выбрать х0 = 2.5

print(method2.iteration(2.5, func_j_0, 10 ** (-10)))
print(method2.iteration(4, func_j_1, 10 ** (-10)))
print(method2.iteration(1, func_v_0, 10 ** (-10)))
print(method2.iteration(1, func_v_1, 10 ** (-10)))







