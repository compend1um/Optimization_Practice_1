def print_header(self, method, root_number, *args):
    methods = {
        "bisection": "Метод деления отрезка пополам",
        "iteration": "Метод простой итерации",
        "newton": "Метод Ньютона"
    }

    print("=" * 40)
    print(f"Функция: {self.name_function}")

    if method == "bisection":

        print( f"Корень {str(root_number)}, отрезок [{args[0]}, {args[1]}]")

    elif method == "iteration":

        print( f"Корень {str(root_number)}, шаг: {args[0]}, х0: {args[1]}")

    elif method == "newton":

        print( f"Корень {str(root_number)}, х0: {args[0]}")

    else:

        exit("направильно набран номер метода")

    print(
        f"{methods[method]}\n",
        "-" * 40,
        sep="",
    )
import os






class BesselFunction:

    def __init__(
            self, function_lambda, name_function, accuracy,

            method1_left_edge_root1, method1_right_edge_root1,
            method1_left_edge_root2, method1_right_edge_root2,

            method2_step_root1, method2_x_base_root1,
            method2_step_root2, method2_x_base_root2,

            method3_x_base_root1,
            method3_x_base_root2,

                ):

        self.name_function = name_function
        self.function_lambda = function_lambda
        self.accuracy = accuracy

        self.method1_left_edge_root1 = method1_left_edge_root1
        self.method1_right_edge_root1 = method1_right_edge_root1
        self.method1_left_edge_root2 = method1_left_edge_root2
        self.method1_right_edge_root2 = method1_right_edge_root2

        self.method2_step_root1 = method2_step_root1
        self.method2_x_base_root1 = method2_x_base_root1
        self.method2_step_root2 = method2_step_root2
        self.method2_x_base_root2 = method2_x_base_root2

        self.method3_x_base_root1 = method3_x_base_root1
        self.method3_x_base_root2 = method3_x_base_root2


    def bisection(self):

        from methods import method1

        print_header(self, "bisection", 1,
                     self.method1_left_edge_root1, self.method1_right_edge_root1)
        method1.find_(self.method1_left_edge_root1, self.method1_right_edge_root1,
                      self.function_lambda, self.accuracy)


        print_header(self, "bisection", 2,
                     self.method1_left_edge_root2, self.method1_right_edge_root2)
        method1.find_(self.method1_left_edge_root2, self.method1_right_edge_root2,
                      self.function_lambda, self.accuracy)



    def iteration(self):

        from methods import method2

        print_header(self, "iteration", 1,
                     self.method2_step_root1, self.method2_x_base_root1)
        method2.iteration(self.function_lambda, self.method2_step_root1,
                          self.method2_x_base_root1, self.accuracy)

        print_header(self, "iteration", 2,
                     self.method2_step_root2, self.method2_x_base_root2)
        method2.iteration(self.function_lambda, self.method2_step_root2,
                          self.method2_x_base_root2, self.accuracy)


    def newton(self):

        from methods import method3

        print_header(self, "newton", 1,
                     self.method3_x_base_root1)
        method3.newton(self.method3_x_base_root1,
                       self.function_lambda, self.accuracy)

        print_header(self, "newton", 2,
                     self.method3_x_base_root2)
        method3.newton(self.method3_x_base_root2,
                       self.function_lambda, self.accuracy)




