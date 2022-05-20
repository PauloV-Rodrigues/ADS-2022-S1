decisao = True
nums = []
valoresDigitados = 0
numerosPares = 0
menorImpar = 9999999999999

while decisao == True:
    num = int(input("Digite um número: "))
    condicao = int(input("Deseja continuar? (1 - Sim | 2 - Não): "))
    nums.append(num)

    valoresDigitados += 1
    if num % 2 == 0:
        numerosPares += 1
    if num % 2 == 1:
        if num < menorImpar:
            menorImpar = num

    if condicao == 1:
        decisao = True
    else:
        decisao = False

print(f"\n\nForam digitados {valoresDigitados} números!")
print(f"{numerosPares} números pares foram digitados!")
print(f"O menor valor ímpar é {menorImpar}!")