a, b, c = float(input()), float(input()), float(input())
d = b**2 - (4 * a * c)
if d < 0 or a == b == 0 and c != 0:
    print("There is no roots")
elif a == b == c == 0:
    print("The equation has infinitely many roots")
elif d == 0 and a != 0:
    x1 = -b / (2 * a)
    print("There is one root:", x1)
elif d > 0 and a != 0:
    x1 = (-b - d**0.5) / (2 * a)
    x2 = (-b + d**0.5) / (2 * a)
    if x1 < x2:
        print("There are two roots:", x1, x2)
    else:
        print("There are two roots:", x2, x1)
elif a == 0:
    print("There is one root:", -c / b)
