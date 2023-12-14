num = 1
rows = 5


for i in range(0, rows):
    for j in range(0, i + 1):
        print(num, end=" ")
        num += 1
        if num > 20:
            break
    print()
