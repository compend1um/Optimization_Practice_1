
import scipy
from utils import BesselFunction


def menu():

    import os

    while True:
        os.system("cls")
        print(
            "=" * 40, "\n",
            "Выберите функцию\n\n"
            "\t1. J0(x)\n",
            "\t2. J1(x)\n",
            "\t3. Y0(x)\n",
            "\t4. Y1(x)\n",
            "\t5. Построить график функции",
            "\n",
            "=" * 40, "\n"
            "\t0. Exit\n",
            sep=""
        )

        select_function = int(input("Select option(0-5):\t"))

        if select_function == 0:

            break

        if select_function not in [1, 2, 3, 4, 5]:

            continue

        os.system("cls")

        # true: блок вычисления корней функций, else: блок построения графиков
        if select_function in [1, 2, 3, 4]:

            print(
                "=" * 40, "\n",
                "Выберите метод\n\n"
                "\t1. Метод деления отрезка пополам\n",
                "\t2. Метод простой итерации\n",
                "\t3. Метод Ньютона\n",
            )

            select_method = int(input("Select option(1-3):\t"))

            if select_method not in [1, 2, 3]: continue

            os.system("cls")

            # j0
            if select_function == 1:

                if select_method == 1: func_j_0.bisection()
                if select_method == 2: func_j_0.iteration()
                if select_method == 3: func_j_0.newton()

                os.system("pause")

            # j1
            if select_function == 2:

                if select_method == 1: func_j_1.bisection()
                if select_method == 2: func_j_1.iteration()
                if select_method == 3: func_j_1.newton()

                os.system("pause")

            # y0
            if select_function == 3:

                if select_method == 1: func_y_0.bisection()
                if select_method == 2: func_y_0.iteration()
                if select_method == 3: func_y_0.newton()

                os.system("pause")

            # y1
            if select_function == 4:

                if select_method == 1: func_y_1.bisection()
                if select_method == 2: func_y_1.iteration()
                if select_method == 3: func_y_1.newton()

                os.system("pause")

        # select_function == 5, построение графиков
        else:

            os.system("cls")
            from utils import build_graph

            print(
                "=" * 40, "\n",
                "Выберите функцию для построения\n\n"
                "\t1. J0(x)\n",
                "\t2. J1(x)\n",
                "\t3. Y0(x)\n",
                "\t4. Y1(x)\n",
            )

            select_grahp_for_build = int(input("Select option(1-4):\t"))

            if select_grahp_for_build == 1:
                build_graph(func_j_0.name_function, func_j_0.function_lambda)

            if select_grahp_for_build == 2:
                build_graph(func_j_1.name_function, func_j_1.function_lambda)

            if select_grahp_for_build == 3:
                build_graph(func_y_0.name_function, func_y_0.function_lambda)

            if select_grahp_for_build == 4:
                build_graph(func_y_1.name_function, func_y_1.function_lambda,
                            -1, 1)


func_j_0_lambda = lambda x: scipy.special.jv(0, x)
func_j_1_lambda = lambda x: scipy.special.jv(1, x)
func_y_0_lambda = lambda x: scipy.special.yv(0, x)
func_y_1_lambda = lambda x: scipy.special.yv(1, x)

func_j_0 = BesselFunction(
    function_lambda=func_j_0_lambda,
    name_function="J0(x)",
    accuracy = 10 ** (-10),

    method1_left_edge_root1 = 0,
    method1_right_edge_root1 = 5,
    method1_left_edge_root2 = 5,
    method1_right_edge_root2 = 7.5,

    method2_step_root1 = -1,
    method2_x_base_root1 = 2,
    method2_step_root2 = 1,
    method2_x_base_root2 = 5.3,

    method3_x_base_root1 = 2,
    method3_x_base_root2 = 5,

)

func_j_1 = BesselFunction(
    function_lambda=func_j_1_lambda,
    name_function="J1(x)",
    accuracy = 10 ** (-10),

    method1_left_edge_root1 = 0,
    method1_right_edge_root1 = 5,
    method1_left_edge_root2 = 5,
    method1_right_edge_root2 = 7.5,

    method2_step_root1 = -1,
    method2_x_base_root1 = 3.2,
    method2_step_root2 = 1,
    method2_x_base_root2 = 7,

    method3_x_base_root1 = 3.2,
    method3_x_base_root2 = 7,

)

func_y_0 = BesselFunction(
    function_lambda=func_y_0_lambda,
    name_function="Y0(x)",
    accuracy = 10 ** (-10),

    method1_left_edge_root1 = 0,
    method1_right_edge_root1 = 5,
    method1_left_edge_root2 = 5,
    method1_right_edge_root2 = 7.5,

    method2_step_root1 = -1,
    method2_x_base_root1 = 3.2,
    method2_step_root2 = 1,
    method2_x_base_root2 = 7,

    method3_x_base_root1 = 3.2,
    method3_x_base_root2 = 7,

)

func_y_1 = BesselFunction(
    function_lambda=func_y_1_lambda,
    name_function="Y1(x)",
    accuracy = 10 ** (-10),

    method1_left_edge_root1 = 0,
    method1_right_edge_root1 = 5,
    method1_left_edge_root2 = 5,
    method1_right_edge_root2 = 7.5,

    method2_step_root1 = -1,
    method2_x_base_root1 = 2,
    method2_step_root2 = 1,
    method2_x_base_root2 = 7,

    method3_x_base_root1 = 2,
    method3_x_base_root2 = 5.5,

)

menu()

