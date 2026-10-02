
import pandas as pd


def find_(a, b, func, accuracy):

    iteration_list = []
    value_list = []
    eps_list = []

    iteration = -1 # первая итерация получит номер 0

    while b - a > accuracy:

        iteration += 1
        center = (a + b) / 2
        eps = (b - a) / 2

        add_iteration(iteration, center, eps, iteration_list, value_list, eps_list)

        if func(center) == 0:
            break

        if func(a) * func(center) < 0:
            b = center

        else:
            a = center

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








