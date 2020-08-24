
def checkRaiz():
    a = int(input("Informe o primeiro coeficiente: "))
    b = int(input("Informe o segundo coeficiente: "))
    c = int(input("Informe o terceiro coeficiente: "))

    delta = (b*b) - (4*a*c)

    if (delta < 0):
        print("Não tem raiz real")
    elif (delta == 0):
        print("Existe uma raiz real")
    else:
        print("Existem duas raizes reais")

checkRaiz()