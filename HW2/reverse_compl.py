seq = [i for i in (input()).upper()]
compl = {"A":"T", "T":"A", "G":"C", "C":"G"}
print("".join([compl.get(n, n) for n in seq][::-1]))
