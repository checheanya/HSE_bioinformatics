a = [1, 3, 2, 6, 4, 5]   # стоимость ступенек
S = [0] * len(a)

S[0] = a[0]
S[1] = a[1]   # наступаем на первую
path = {}
for i in range(2, len(S)):
    S[i] = min(S[i - 1], S[i - 2]) + a[i]
    if min(S[i - 1], S[i - 2]) == S[i - 1]:
        path[i] = i - 1   # записываем в словарь [номер ступеньки, номер ступеньки откуда пришли]
    else:
        path[i] = i - 2

print(path)

l = []
h = len(S) - 1
while h != 2:
    fr = path[h]
    l.append(h - path[h]) # записываем в итоговый список длину шага, нач с конца
    h = fr
print(l)

for i in range(len(l)):
    if l[i] == 1:
        l[i] = "одна ступенька"
    else:
        l[i] = "две ступеньки"
print(*['одна ступенька', 'одна ступенька'], *l[::-1])


# в какой-то домахе понадобятся геномные повторы из генбанка
