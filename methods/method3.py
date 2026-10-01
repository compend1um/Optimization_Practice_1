import scipy

def iteration(x_base, func, eps):
    m = scipy.differentiate.derivative(func, x_base).df

    while True:
        x_new = x_base - func(x_base) / m
        if abs(x_new - x_base) < eps:
            return x_new
        x_base = x_new


