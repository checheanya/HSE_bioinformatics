'''
seq = input('Введите последовательность: ').replace('\n', '')
suff = input(list(map(int, input('Введите суффиксный массив: ').split(', '))))
'''


seq = 'ATATATTAG'
suff = [10, 8, 1, 3, 5, 9, 7, 2, 4, 6]


def Bar_Wee(seq, suff):
    bwt = list([0]*(len(seq) + 1))
    for i in range(len(suff)):
        if suff[i] == 1:
            bwt[i] = '$'
        else:
            bwt[i] = seq[suff[i] - 2]
    return ('').join(bwt)


def C_func(letter):
    seq_l = list(i for i in seq)
    if letter in seq:
        return sorted(seq_l).index(letter) + 1
    else:
        seq_l = sorted(seq_l + ['A', 'C', 'G', 'T'])
        return seq_l.index(letter) - ['A', 'C', 'G', 'T'].index(letter) + 1


print('BWT(X) =', Bar_Wee(seq, suff))
print('C($) = 0', 'C(A) =', C_func('A'), 'C(C) =', C_func('C'), 'C(G) =', C_func('G'), 'C(T) =', C_func('T'))
