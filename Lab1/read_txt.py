import numpy as np

def read_txt():
    with open('file.txt', 'r') as f:
        s = f.readline()
        data = np.loadtxt(f)

    x = data[:, 0]
    y = data[:, 1]

    M = np.vstack([x, y])
    print(M)

    return M

