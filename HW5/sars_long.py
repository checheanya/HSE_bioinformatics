seqs = open("sars_genes.gff", 'r')
lines = seqs.readlines()
seqs.close()
print(lines)
res = list()
for i in lines:
    if i[0] != '#':        # не смотрим строки, нач на #
        i = i.split('\t')  # переводим в список - столбцы
        if i[2] == 'gene':
            name_pos = i[8].find('Name') + 5   # начало
            name = i[8][name_pos:i[8].find(';', name_pos)]    # имя
            res.append([int(i[4]) - int(i[3]), name])

for t in res:
    print(t[1], t[0])
