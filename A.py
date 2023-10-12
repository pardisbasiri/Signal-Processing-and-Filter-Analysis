import numpy as np
import matplotlib.pyplot as plt


def moving_average_impulse_response(x, p):
    if 2 * p >= x >= 0:
        return 1
    return 0


def discrete_fourier_transform(filter, k):
    res = []
    for i in range(k):
        res += [0]
    for i in range(k):
        for j in range(-100, 100):
            res[i] += filter(j, 4) * np.exp(2j * np.pi * i * j / k)
    return res


final_res = discrete_fourier_transform(moving_average_impulse_response, 1024)  #the number of samples(k) should be 1024 minimum
plt.plot(np.abs(final_res))                                                    # using abs because we want the absolute value
plt.show()