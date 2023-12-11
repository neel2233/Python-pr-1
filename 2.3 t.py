
a = int(input("Введите кол-во ступенек: "))
for i in range(1, a+1):
    for j in range(1, i+1):

        print(j, end='')
    if len(str(i + 2)) > 1:
        print("\n" * (len(str(i + 2)) - 1), end="")
    print()
