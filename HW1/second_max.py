n = int(input())
max1 = float(input())
max2 = float(input())
for i in range(n-2):
    a = float(input())
    if max1 < a:
        max2 = max1
        max1 = a
    elif max2 < a != max1:
        max2 = a
print(max2)
