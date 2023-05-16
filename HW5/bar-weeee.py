seq = input()

var = list()
for i in range(len(seq)): # все варианты сдвигов
    u = seq[i:] + seq[:i]
    var.append(u)
var.sort()

result = str()
for i in var:
    result += i[-1]
print(result)
