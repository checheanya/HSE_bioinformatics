a = [i for i in (input()).upper()]
b = [i for i in (input()).upper()]

match, mut, gap = 5, -4, -10

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
        if a[j - 1] == b[i - 1]:
            step = match
        else:
            step = mut
        matrix[i][j] = max(matrix[i - 1][j - 1] + step, matrix[i][j - 1] + gap, matrix[i - 1][j] + gap)

for j in matrix:
    print(*j)
