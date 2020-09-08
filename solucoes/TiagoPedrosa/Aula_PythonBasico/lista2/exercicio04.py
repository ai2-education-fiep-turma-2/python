def Adicao():
    a = int(input("Informe o primeiro numero: "))
    b = int(input("Informe o segundo numero: "))
    total = a + b

    if (total > 20):
        total += 8
    else:
        total -= 5
    print(total)
Adicao()