def menorNumero():
    a = int(input("Digite o primeiro númenro: "))
    b = int(input("Digite o primeiro númenro: "))
    if (a < b):
        print(a, "é menor número")
    elif (b < a):
        print(b, "é menor númenro")
    else:
        print("Os dois números são iguais")

menorNumero()