decisao = True
idades = []
valoresDigitados = 0
somaIdade = 0
maiorQueVinteUm = 0


while decisao == True:
    idade = int(input("Digite uma idade: "))
    condicao = int(input("Deseja continuar? (1 - Sim | 2 - Não): "))
    idades.append(idade)

    valoresDigitados += 1
    somaIdade += idade
    if idade > 21:
        maiorQueVinteUm += 1

    if condicao == 1:
        decisao = True
    else:
        decisao = False

print(f"Foram digitados {valoresDigitados} idades!")
print("A média de idades é {:.1f}!".format(somaIdade/valoresDigitados))
print(f"{maiorQueVinteUm} pessoas possuem mais de 21 anos!")