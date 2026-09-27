def find_(a, b, func, eps):
    """
    :param a: конец левый
    :param b: коней правый
    :param func: функция
    :param eps: требуемая погрешность
    :return: корен функции, лежащий в промежутке
    """

    while b - a > eps:

        center = (a + b) / 2

        if func(center) == 0:
            return center
        if func(a) * func(center) < 0:
            b = center

        else:
            a = center

    return (a + b) / 2






