align = [[0, 0] for i in range(5)]
align[-1][1] = 90
upp = []
dow = []
for i in align:
    upp.append(str(i[0]))
    dow.append(str(i[1]))
print(''.join(upp))
print(*dow)