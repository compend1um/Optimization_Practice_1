
import pandas as pd


def iteration(func, step, x_base, accuracy):

    iteration_list = []
    value_list = []
    eps_list = []

    iteration_number = -1 # первая итерация получит номер 0


    while True:

        iteration_number += 1
        x_new = x_base - step * func(x_base)
        eps = (x_new - x_base) / 2

        add_iteration(iteration_number, x_new, eps, iteration_list, value_list, eps_list)


        if abs(x_new - x_base) < accuracy:
            break

        x_base = x_new

    print_result(iteration_list, value_list, eps_list)

def add_iteration(iteration_number, center, eps, iter_list:list, val_list:list, eps_list:list):
    iter_list.append(iteration_number)
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


