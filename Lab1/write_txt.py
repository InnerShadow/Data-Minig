import numpy as np

def write_txt():
    x = np.arange(0, 5, 0.1)
    y = 2 * x ** 2 + x - 1
    M = np.vstack([x, y])

    with open('file.txt', 'w') as f:
        f.write('function 2 * x ** 2 + x - 1\n')
        np.savetxt(f, M.T, fmt = '%.3f')

