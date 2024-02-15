import numpy as np

def myfunc(X_left, X_right, Y_left, Y_right, N):
    X = X_left + np.random.uniform(0, 1, size = N) * (X_right - X_left)
    Y = Y_left + np.random.uniform(0, 1, size = N) * (Y_right - Y_left)

    return X, Y

