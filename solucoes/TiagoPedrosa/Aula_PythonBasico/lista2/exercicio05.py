
def square():
    from math import sqrt
    numero = int(input("Digite um numero: "))

    if (numero >=0):
        result = sqrt(numero)
    else:
        result = numero ** 2
    
    print("O resultado é ", result)

square()