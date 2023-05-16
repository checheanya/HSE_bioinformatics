n = int(input())
m = float(input())
for i in range(n-1):
    a = float(input())
    if a > m:
        m = a
print("The maximum is", m)
