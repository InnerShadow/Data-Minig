import numpy as np

def matrix():
    V = np.array([1, 2, 3, 4, 5])
    M = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9 ,10], [11, 12, 13, 14, 15]])

    print(f"Vec = \n{V}\n")
    print(f"MAtrix = \n{M}\n")

    print(V[2], '\n')
    print(M[2, 3], '\n')
    print(M[2, :], '\n')

    S = np.array([1, 2, 3, 4, 5])
    M = np.vstack([M, S])
    print(f'Add row to matrix:\n {M}\n')

    S = np.array([1, 2, 3, 4])
    S = np.transpose([S])  # Транспонирование для превращения в вертикальный столбец
    M = np.hstack([M, S])
    print(f'Add colum to matrix:\n {M}\n')

    M = np.delete(M, -1, axis = 0)
    M = np.delete(M, -1, axis = 1)
    print(f'Delite row & colum... \n{M}\n')

    print(f'Max by row: {np.max(M, axis = 1)}')
    print(f'Min by col: {np.min(M, axis = 0)}')
    print(f'Max in all matrix: {np.amax(M)}\n')

    
def create_matrix():
    M = np.zeros([5, 5])
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i, j] = np.random.randint(0, 1000)

    print(f"Matrix: \n{M}\n")
    return M


def get_max(M, axsi = 0):
    return np.max(M, axis = axsi)


def get_min(M, axis = 0):
    return np.min(M, axis = axis)

def get_matrix_min(M):
    return np.amin(M)


def get_matrix_max(M):
    return np.amax(M) 


def solve(): 
    A = np.array([[2, 1], [3, 4]])
    B = np.array([4, 11])

    return np.linalg.inv(A) * B.T