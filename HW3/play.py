import numpy as np


a = [i for i in (input('Введите последовательность 2: ')).upper()]
b = [i for i in (input('Введите последовательность 2: ')).upper()]
"""

a = [i for i in 'ATCCGAGTT'.upper()]
b = [i for i in 'ATCAGTC'.upper()]
"""
matr_shtr = "DNAfull"


def step(a, b):  # выбор матрицы штрафов
    if matr_shtr == "DNAfull":
        if a == b:
            k = 5
        else:
            k = -4
    if matr_shtr == "Purin-pirimidin":
        if a == b:
            k = 2
        elif (a == 'G' and b == 'C') or (a == 'C' and b == 'G') or (a == 'A' and b == 'G') or (a == 'G' and b == 'A'):
            k = -1
        else:
            k = -2
    return k


def arrow(i, j):  # указываем, откуда пришли
    if max(matrix[i - 1, j - 1, 0] + step(a[j - 1], b[i - 1]), matrix[i, j - 1, 0] + gap,
           matrix[i - 1, j, 0] + gap) == matrix[i - 1, j - 1, 0] + step(a[j - 1], b[i - 1]):
        g = 0  # diag
    if max(matrix[i - 1, j - 1, 0] + step(a[j - 1], b[i - 1]), matrix[i, j - 1, 0] + gap,
           matrix[i - 1, j, 0] + gap) == matrix[i, j - 1, 0] + gap:
        g = -1  # right
    else:
        g = 1  # down
    return g


gap = -10
e = 0

leng = len(a) + 1
high = len(b) + 1
matrix = np.zeros((high, leng, 2))

if e == 0: # для линейной
    matrix[0] = [[i * gap, 0] for i in range(leng)]

    for i in range(1, high):
        matrix[i, 0, 0] = i * (-10)

    for i in range(1, high):
        for j in range(1, leng):
            matrix[i, j, 0] = max(matrix[i - 1, j - 1, 0] + step(a[j - 1], b[i - 1]), matrix[i, j - 1, 0] + gap,
                                  matrix[i - 1, j, 0] + gap)
            matrix[i, j, 1] = arrow(i, j)

#else [[gap + (i - 1) * e, 0] for i in range(leng)]

#print(matrix)

score = matrix[-1, -1, 0]
print('Score: ', score)

# строим само выравнивание
align = [[0, 0] for i in range(len(a)+len(b))]
i, j = -1, -1

while i != 1 and j != 1:
    if matrix[i, j, 1] == 0:
        align[j][0] = a[-1]
        align[j][1] = b[-1]
        a = a[:-1]
        b = b[:-1]
        i -= 1
        j -= 1
    elif matrix[i, j, 1] == 1:
        align[j][0] = "-"
        align[j][1] = b[-1]
        b = b[:-1]
        i -= 1
        j -= 0
    elif matrix[i, j, 1] == -1:
        align[j][0] = a[-1]
        align[j][1] = "-"
        b = b[:-1]
        i -= 0
        j -= 1
upp = []
dow = []
for i in align:
    upp.append(str(i[0]))
    dow.append(str(i[1]))
print(''.join(upp))
print(''.join(dow))
