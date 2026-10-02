import numpy, scipy, matplotlib
from base_class import BesselFunction

import calls.meths1
import calls.meths2
from methods import method3
from calls import meths1

func_j_0_lambda = lambda x: scipy.special.jv(0, x)
# func_j_1_lambda = lambda x: scipy.special.jv(1, x)
# func_y_0_lambda = lambda x: scipy.special.yv(0, x)
# func_y_1_lambda = lambda x: scipy.special.yv(1, x)

func_j_0 = BesselFunction(
    function_lambda=func_j_0_lambda,
    name_function="J0(x)",
    accuracy = 10 ** (-10),

    method1_left_edge_root1 = 0,
    method1_right_edge_root1 = 5,
    method1_left_edge_root2 = 5,
    method1_right_edge_root2 = 7.5,

    method2_step = -0.01,
    method2_x_base = 2,

)

func_j_0.bisection()
# метод 1

# calls.meths1.print_()



# пример печати, надо еще три таких же



# method 2, выбрать х0 = 2.5

# calls.meths2.print_()




# print(method3.iteration(2.5, func_j_0, 10 ** (-10)))
# print(method3.iteration(4, func_j_1, 10 ** (-10)))
# print(method3.iteration(1, func_v_0, 10 ** (-10)))
# print(method3.iteration(1, func_v_1, 10 ** (-10)))







