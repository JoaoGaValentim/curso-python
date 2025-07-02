for i in range(100):
    if i % 2 == 1:
        print("Impar ignorado...")
        continue

    if i % 2 == 0:
        print(i)
        for j in range(1, 3):
            print(i, j)

    if i == 98:
        break

else:
    print("Fim do For")
