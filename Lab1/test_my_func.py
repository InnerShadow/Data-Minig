import numpy as np
import matplotlib.pyplot as plt
from my_func import *

def test_my_func(X_left, X_right, Y_left, Y_right, x, y):
    BinNumber = 20
    k = np.arange(0, BinNumber)

    X_bin = X_left + k * (X_right - X_left) / BinNumber
    Y_bin = Y_left + k * (Y_right - Y_left) / BinNumber

    plt.figure(figsize = (8, 4))

    plt.subplot(1, 2, 1)
    plt.hist(x, bins = X_bin)
    plt.title('X hist')
    plt.xlabel('X values')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.hist(y, bins = Y_bin)
    plt.title('Y hist')
    plt.xlabel('Y values')
    plt.ylabel('Frequency')

    plt.show()

