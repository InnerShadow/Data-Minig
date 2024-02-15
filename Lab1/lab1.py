from test_matrix import *
from test_graphic import *
from vrosenbrock import *
from my_func import *
from test_my_func import *
from my_gauss_gen import *
from test_cycle import *
from write_txt import *
from read_txt import *

def main():
    '''
        Получите справку по следующим операциям и функциям: ^,
        asin, inv, plot.
    '''

    # help(np.power)
    # help(np.arcsin)
    # help(np.linalg.inv)
    # help(plt.plot)

    '''
        Введите в test_matrix.m описанные выше процедуры объ-
        явления вектора и матрицы, процедуры доступа к элементам вектора и
        матрицы, поиск минимального и максимального элемента в матрице. Про-
        смотрите результат в командном окне.
        Добавьте в test_matrix.m код, добавляющий и удаляющий вектор к
        матрице.
    '''
    matrix()

    '''
        Объявите матрицу C размерности 5 строк на 5 столбцов с
        произвольными элементами. С помощью функций min, max найдите ми-
        нимальные и максимальные элементы по строкам, по столбцам и по всей
        матрице.
    '''
    M = create_matrix()
    print(f'Max by row: {get_max(M, 1)}, by col = {get_max(M, 0)}\n')
    print(f'Min by row: {get_min(M, 1)}, by col = {get_min(M, 0)}\n')
    print(f'Min in all matrix: {get_matrix_min(M)}, max = {get_matrix_max(M)}\n\n')


    '''
        Получить решение x заданной системы линейных уравне-
        ний вида A* x = B, где A – квадратная матрица n n, B – вектор размерно-
        сти n. Решение данной системы уравнений можно получить, набрав строку
        кода
    '''

    print(f"Solve: \n{solve()}\n\n")

    '''
        Создайте файл test_graphic.m, в котором наберите приве-
        денный код п. 10. Сохраните полученный график в формате tiff с разреше-
        нием 200 dpi (имя файла произвольное).
    '''

    test_graphic()

    '''
        3D graph
    '''

    graph()

    '''
        Задание 10. Создайте новый m-файл и сохраните его под именем
        my_func. В файле поместите размещенное выше описание функции
        my_func.
    '''

    X_lift, X_right, Y_left, Y_right, N = 0, 5, 6, 10, 1000

    x, y = myfunc(X_lift, X_right, Y_left, Y_right, N)
    plt.scatter(x, y)
    plt.show()

    '''
        Задание 11. Создайте файл test_my_func.m, в котором наберите код,
        демонстрирующий работу функции my_func. Запустите программу и про-
        смотрите результат ее работы.
        Создайте заголовки гистограмм и подписи по осям с помощью функ-
        ций title, xlabel, ylabel, добавив их после функции bar.
    '''

    test_my_func(X_lift, X_right, Y_left, Y_right, x, y)

    '''
        Создайте функцию my_gauss_gen, которая генерирует за-
        данное количество случайных величин N, имеющих гауссовское распре-
        деление с заданным математическим ожиданием m и дисперсией D. По-
        стройте гистограмму (рис. 1.3).
    '''

    my_gauss_gen(0, 1, 1000)

    '''
        Задание 13. Создайте файл test_cycle.m, в котором сформируйте мат-
        рицу Q произвольного размера и заполните ее случайными целыми чис-
        лами. Выведите в главном окне MATLAB (Command Window) матрицу Q
        (добавьте в код команду disp(Q)).
    '''

    '''
        Задание 14. В файле test_cycle.m реализуйте цикл, позволяющий вы-
        числять сумму элементов матрицы Q. Весь необходимый код напишите в
        файле test_cycle.m.
    '''

    test_cycle(10, 3)

    '''
        Задание 15. Создайте новый m-файл с именем write_txt, в котором на-
        берите код записи данных с помощью функции fprintf. Запустите код на
        выполнение (клавиша F5). Откройте созданный текстовый файл и убеди-
        тесь, что запись прошла корректно (в файле есть данные).
    '''

    write_txt()

    '''
        Задание 16. Создайте новый m-файл с именем read_txt, в котором на-
        берите код считывания из файла с помощью fscanf. Запустите программу
        14на выполнение (клавиша F5). Выведите на экран матрицу данных из фай-
        ла.
    '''

    read_txt()


if __name__ == '__main__':
    main()

