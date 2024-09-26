def multSum():
    limite = (int(input("Limite: ")))
    soma = 0
    for i in range(0,limite + 1):
        if (i % 3 == 0 or i % 5 == 0):
            soma += i
    print("A soma é ", soma)
multSum()