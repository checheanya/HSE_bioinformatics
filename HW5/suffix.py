seq = input()

var = ['$' + seq]
for i in range(len(seq)): # все варианты сдвигов
    u = seq[i:] + '$' + seq[:i]
    var.append(u)
var.sort()

result = list()
for i in var:
    result.append(len(i) - i.find('$'))
print(result)
