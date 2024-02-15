import matplotlib.pyplot as plt
import numpy as np

def test_graphic():
    x = np.arange(0, 6.28, 0.1)
    y = np.sin(x)

    plt.plot(x, y)
    plt.grid(True)
    plt.title('Function sin(x)')
    plt.xlabel('Argument x')
    plt.ylabel('Function y')

    plt.savefig('graph.tiff', dpi = 200, format = "tiff")

    plt.show()

    pass

