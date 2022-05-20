def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

vetorNumerico = []

for i in range(16):
    vetorNumerico.append(rec_fib(i))

print(vetorNumerico)