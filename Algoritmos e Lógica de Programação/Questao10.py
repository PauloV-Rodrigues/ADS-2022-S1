import random
i = int(input("Quantos números vamos sortear? "))
x = 1

sorteio = []
maiorQueCinco = []
divisivelPorTres = []

while x <= i:
    sorteio.append(random.randint(0, 50))
    x += 1
print(f"Números sorteados: {sorteio}")

for j in sorteio:
    if j > 5:
        maiorQueCinco.append(j)
print(f"Números maiores que cinco: {maiorQueCinco}")

for k in sorteio:
    if k % 3 == 0:
        divisivelPorTres.append(k)
print(f"Números divisíveis por três: {divisivelPorTres}")