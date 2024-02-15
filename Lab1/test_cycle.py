import numpy as np

def test_cycle(n, m):
    Q = np.zeros((n, m))
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            Q[i, j] = np.random.randint(0, 1000)

    print(f'Q is : \n{Q}')

    s = 0
    for i in Q:
        for j in i:
            s += j

    print(f'Sum: {s}')
    return s

