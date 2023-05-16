dct = {'b': ['k'], 'c': []}
is_empty = []
for key in dct.keys():
    is_empty.append(len(dct[key]))
print(is_empty == list([0]*(len(dct.keys()))))