vetorNumerico = []
j = 5
k = 3
current  = 0

vetorNumerico.append(j)
for i in range(9):
    if vetorNumerico[current] == j:
        vetorNumerico.append(k)
    else:
        vetorNumerico.append(j)
    current += 1
    
print(vetorNumerico)
