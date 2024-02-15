import numpy as np
import matplotlib.pyplot as plt

def my_gauss_gen(m, var, N):
    X = np.random.normal(m, var, size = N)

    BinNumber = 20
    k = np.arange(0, BinNumber)
    bin = np.min(X) + k * (np.max(X) - np.min(X)) / BinNumber

    plt.hist(X, bins = bin)
    plt.title('Normal distribution hist')
    plt.xlabel('X values')
    plt.ylabel('Frequency')
    plt.show()

