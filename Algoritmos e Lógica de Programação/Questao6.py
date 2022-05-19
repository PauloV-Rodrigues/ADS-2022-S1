i = 30

while i >= 1:
    if i % 4 == 0:
        print(f"[{i}]", end=" ")
        i -= 1
    else:
        print(i, end=" ")
        i -= 1
