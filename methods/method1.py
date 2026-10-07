
import pandas as pd


# главная функция, печатает результат вычислений методом деления пополам
def find_(a, b, func, accuracy):

    # листы для печати результата пандасом
    iteration_list = []
    value_list = []
    eps_list = []

    iteration = -1 # первая итерация получит номер 0

    while b - a > accuracy:

        iteration += 1
        center = (a + b) / 2
        eps = (b - a) / 2

        add_iteration(iteration, center, eps, iteration_list, value_list, eps_list)

        # левый край и центр разных знаков - корень в левой половине, правый край надо перенасти на место центра
        if func(a) * func(center) < 0:
            b = center

        # корень в правой половине, сдвигаем границу слева на центр
        else:
            a = center

    # погрешность менее 10 ** (-10), вышли из цикла, печатаем результат
    print_result(iteration_list, value_list, eps_list)

    return None


# компактная запись данных текущей итерации в списки для печати пандаса
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

    # печать eps в формате float с 10 знаками после запятой
    pd.set_option("display.float_format", lambda x: f"{x:.12f}")

    print(df.to_string(index=False))

    print(
        "\n",
        "Найденный корень: х =", f"{value_list[-1]}",
        "\n",
    )








