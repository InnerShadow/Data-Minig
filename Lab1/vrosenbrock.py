import matplotlib.pyplot as plt
import numpy as np

def vrosenbrock(x, y):
    return 100 * (y - x ** 2) ** 2 + (1 - x) ** 2


def graph():
    xs = np.arange(-5, 5, 0.05)
    ys = np.arange(-5, 5, 0.05)

    x, y = np.meshgrid(xs, ys)
    z = vrosenbrock(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    surf = ax.plot_surface(x, y, z)

    fig.colorbar(surf)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    plt.show()
    pass

