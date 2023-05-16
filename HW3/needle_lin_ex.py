"""
a = [i for i in (input()).upper()]
b = [i for i in (input()).upper()]
"""

a = [i for i in 'ATCCGAGTT'.upper()]
b = [i for i in 'ATCAGTC'.upper()]


def step(a, b):
    if a == b:
        k = 2
    elif (a == 'G' and b == 'C') or (a == 'C' and b == 'G') or (a == 'A' and b == 'G') or (a == 'G' and b == 'A'):
        k = -1
    else:
        k = -2
    return k

gap = -10

leng = len(a) + 1
high = len(b) + 1
matrix = []
for i in range(high):
    zero_row = [0] * leng
    matrix.append(zero_row)

matrix[0] = [i * (-10) for i in range(leng)]

for i in range(1, high):
    matrix[i][0] = i * (-10)

for i in range(1, high):
    for j in range(1, leng):
        matrix[i][j] = max(matrix[i - 1][j - 1] + step(a[j - 1], b[i - 1]), matrix[i][j - 1] + gap,
                           matrix[i - 1][j] + gap)

for j in matrix:
    print(*j)
