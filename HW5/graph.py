seqs = open("our2.fastq", 'r')
lines = seqs.readlines()
seqs.close()

k = int(input())

# режем риды на k-меры
all_seq = lines[1::4]

doubled = dict()

# k-1 вершины графа - ключи, К- грани - значения
for seq in all_seq:
    seq = seq.replace('\n', '')
    for i in range(len(seq) - (k-2)):
        if seq[i:i+k-1] in doubled.keys():
            if i == (len(seq) - (k-2) - 1):
                continue
            else:
                doubled[seq[i:i+k-1]].append(seq[i:i+k])
        else:
            if i == (len(seq) - (k-2) - 1):
                doubled[seq[i:i+k-1]] = []
            else:
                doubled[seq[i:i+k-1]] = [seq[i:i+k]]


def new(edge_list):
    doubled_new = doubled.copy()
    for key in doubled_new.keys():
        for mer in doubled_new[key]:
            if mer in edge_list:
                doubled_new[key].remove(mer)
    return doubled_new


def path(key_from, key_from_list, edge_list):
    doubled_new = new(edge_list)
    while not (key_from in key_from_list) and not(len(doubled_new[key_from]) == 0):
        if len(doubled_new[key_from]) == 1:
            key_to = doubled_new[key_from][0][1:]
            key_from_list.append(key_from)
            edge_list.append(doubled_new[key_from][0])
            key_from = key_to
            doubled_new[key_from] = []
        else:
            key_to = doubled_new[key_from][0][1:]
            key_from_list.append(key_from)
            edge_list.append(doubled_new[key_from][0])
            doubled_new[key_from] = doubled_new[key_from][1:]
            key_from = key_to

    for key in key_from_list:
        if len(doubled_new[key]) != 0:
            # даблд нью равен
            return path(doubled_new[key][0][1:], key_from_list[:key_from_list.index(key) + 1],
                        edge_list[:key_from_list.index(key) + 1])
        else:
            continue
    return "nashel"

key_from = all_seq[0][:k - 1]
key_from_list = []
edge_list = []

print(path(key_from, key_from_list, edge_list))

"""
list_for_path = list([0]*(len(multiple_list)))
for mer in multiple_list:
    mer[]
print(doubled)
print(multiple_list)

# проходим по ключам словаря
final = [all_seq[0][:k-1]]
key_from = all_seq[0][:k-1]
result = []

for keys in dict_for_path.keys():
    for foo in dict_for_path[keys]:
        while len(doubled[key_from]) != 0:
            if len(doubled[key_from]) == 1:
                key_to = doubled[key_from][0][1:]
                final.append(doubled[key_from][0][-1])
                doubled[key_from] = []
            else:
                key_to = doubled[key_from][foo][1:]
                final.append(doubled[key_from][foo][-1])
                doubled[key_from] = doubled[key_from][1:]
            key_from = key_to
            result.append(''.join(final))
        if len(final) == count:
            print(final)
            break
        else:
            continue

for var in result:
    if len(var) == count:
        print(var)
"""
