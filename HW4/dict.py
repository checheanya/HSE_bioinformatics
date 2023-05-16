sars = open('all_sars.txt', 'r')
seq = [i for i in sars.read()]
print('Длина генома {} пн'.format(len(seq)))
k = int(input('Введите размер подпоследовательности: '))

print(seq)

doubled = dict()
for i in range(len(seq) - k):
    if ''.join(seq[i:i+k+1]) in doubled.keys():
        doubled[''.join(seq[i:i+k+1])].append(i)
    else:
        doubled[''.join(seq[i:i+k+1])] = [i]

for k in doubled.keys():
    print(str(k) + str(doubled[k]))