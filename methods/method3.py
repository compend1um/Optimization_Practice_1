import scipy
import pandas as pd


def newton(x_base, func, accuracy):

    iteration_list = []
    value_list = []
    eps_list = []

    m = scipy.differentiate.derivative(func, x_base).df
    iteration = -1 #первая иторация = 0


    while True:

        iteration += 1
        x_new = x_base - func(x_base) / m
        eps = abs( (x_new - x_base) / 2 )

        add_iteration(iteration, x_new, eps, iteration_list, value_list, eps_list)

        if abs(x_new - x_base) < accuracy:
            break

        x_base = x_new

    print_result(iteration_list, value_list, eps_list)

    return None


def add_iteration(iteration, center, eps, iter_list:list, val_list:list, eps_list:list):
    iter_list.append(iteration)
    val_list.append(center)
    eps_list.append(eps)


def print_result(iteration_list, value_list, eps_list):
    df = pd.DataFrame({
        "ITR": iteration_list,
        "VAL": value_list,
        "EPS": eps_list
    })

    pd.set_option("display.float_format", lambda x: f"{x:.10f}")

    print(df.to_string(index=False))

    print(
        "\n",
        "Найденный корень: х =", value_list[-1],
        "\n",
    )




