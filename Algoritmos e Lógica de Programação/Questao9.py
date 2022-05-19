i = int(input("Digite até onde deseja contar: "))
j = 1
while j <= i:
    if j % 4 == 0:
        print("PIN! -", end=" ")
        j += 1
    else:
        print(f"{j} -", end=" ")
        j += 1