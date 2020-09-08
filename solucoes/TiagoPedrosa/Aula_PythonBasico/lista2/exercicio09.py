def showNumbers():
    limite = (int(input("Limite: ")))

    for i in range(0,limite + 1):
        if (i % 2 == 0):
            print(i, "- PAR")
        else:
            print(i, "- IMPAR")

showNumbers()