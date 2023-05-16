a = [i for i in range(101)]
while 1 == 1:
    print("Is your number less than {}?".format(a[(len(a) - 1) // 2]))
    n = input()
    if n == "Yes":
        a = a[:(len(a) - 1) // 2]
    elif n == "No":
        a = a[(len(a) - 1) // 2:]
    if len(a) <= 2:
        print("So your number is {}, right?".format(a[0]))
        n = input()
        if n == "Yes":
            print("Great!")
            break
        else:
            print("I was really close, it's", a[1])
            break
"""
строим дерево - число листиков 101 (бинарное)
глубина не может быть меньше, чем log2(101) = 6.7 - округляем до 7
"""