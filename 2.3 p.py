n = int(input("Введите кол-во ступенек: "))
t = ""
for j in range(1, n):
    t += str(j)
for j in range(n, 0, -1):
    if j % 10 == 0:
        t += " " + str(j)
    else:
        t += str(j)
width = len(t)

for i in range(n):
    x = ""
    for j in range(1, i + 1):
        x += str(j)
    for j in range(i + 1, 0, -1):
        if j % 10 == 0:
            x += " " + str(j)
        else:
            x += str(j)
    print(x.center(width))
    if len(str(i + 2)) > 1:
        print("\n" * (len(str(i + 2)) - 1), end="")
