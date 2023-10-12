import numpy as np
import matplotlib.pyplot as plt


def filter_low_pass(x):
    p = 300
    omega = np.pi / 8
    if x == 300:         # for handling lim 0/0
        return 0.125
    if 2 * p >= x >= 0:
        return (np.sin(omega * (x - p))) / (np.pi * (x - p))
    return 0


def discrete_fourier_transform(filter, k):
    result = []
    for i in range(k):
        result += [0]
    for i in range(k):
        for j in range(-1000, 1000):
            result[i] += filter(j) * np.exp(2j * np.pi * i * j / k)
    return result


final_res = discrete_fourier_transform(filter_low_pass, 1024)    # sample count (k) should be 1024 minimum
plt.plot(np.abs(final_res))                                      # using abs because we want the absolute value
plt.show()
