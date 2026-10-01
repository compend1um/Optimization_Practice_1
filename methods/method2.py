
def iteration(func, step, x_base, eps):
    while True:
        x_new = x_base - step * func(x_base)

        if abs(x_new - x_base) < eps:
            return x_new

        x_base = x_new


