i = float(input("Onde começa a contagem: "))
j = float(input("Onde termina a contagem: "))
x = float(input("Qual o incremento: "))

while i <= j:
    print('{:.0f}'.format(i), end=" ")
    i += x

print("FIM!")