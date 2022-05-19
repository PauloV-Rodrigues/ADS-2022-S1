i = int(input("Digite o primeiro valor: "))
j = int(input("Digite o último valor: "))
x = int(input("Digite o incremento: "))

for i in range(i, j+1, x):
    print(i, end=" ")

print("Acabou!")