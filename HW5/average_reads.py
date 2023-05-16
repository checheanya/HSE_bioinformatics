seqs = open("sars_genes.gff", 'r')
lines = seqs.readlines()
seqs.close()

f = open("coverage.tsv")
reads = f.readlines()
f.close()

res = list()
for i in lines:
    if i[0] != '#':        # не смотрим строки, нач на #
        i = i.split('\t')  # переводим в список - столбцы
        if i[2] == 'gene':
            name_pos = i[8].find('Name') + 5   # начало
            name = i[8][name_pos:i[8].find(';', name_pos)]    # имя
            res.append([int(i[4]) - int(i[3]), name])

res_cover = list()
for j in reads:
    j = j.replace('\n', '').split('\t')    # разделяем по строкам
    res_cover.append([int(j[1]), j[0]])

for gene in res:
    for cov in res_cover:
        if gene[1] == cov[1]:
            print(gene[1], 'Coverage:', cov[0]/gene[0])
