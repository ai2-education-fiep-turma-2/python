def menu():
    opcao = int(input("Digite o número do exercicio (1-10) ou 0 para sair: "))
    
    if opcao == 1:
        exercicio1()
    elif opcao == 2:
        exercicio2()
    elif opcao == 3:
        exercicio3()
    elif opcao == 4:
        exercicio4()
    elif opcao == 5:
        exercicio5()
    elif opcao == 6:
        exercicio6()
    elif opcao == 7:
        exercicio7()
    elif opcao == 8:
        exercicio8()
    elif opcao == 9:
        exercicio9()
    elif opcao == 10:
        exercicio10()
    # elif opcao == 11:
    #     exercicio11()
    elif opcao == 0:
        sair()
    else:
        "Opção inválida"

def sair():
    import sys
    sys.exit()

def exercicio1():
    for i in range(1,100):
        if i % 2 != 0:
            print(i)
    menu()

def exercicio2():
    nome = input("Digite seu nome: ")
    print("Bem vindo", nome)
    menu()

def exercicio3():
    for i in range(1,51):
        print(i)
    menu()

def exercicio4():
    numero1 = int(input("Primeiro número:"))
    numero2 = int(input("Segundo número:"))

    soma = numero1 + numero2
    prod = numero1 * numero2
    quo = numero1 / numero2
    rest = numero1 % numero2
    print("Soma:", soma, "Produto:", prod, "Quociente:", quo, "Resto", rest)
    menu()
    
def exercicio5():
    carac = input("Digite o caracter: ").lower()

    if carac == 'y':
        print("YES!")
    elif carac == 'n':
        print("NÃO!")
    else:
        print("Não conheço")

    menu()

def exercicio6():
    lado1 = float(input("Primeiro lado: "))
    lado2 = float(input("Segundo lado: "))
    lado3 = float(input("Terceiro lado: "))

    if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
        print("Triângulo equilátero")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("Triângulo escaleno")
    else:
        print("Triângulo isósceles")

    menu()

    
def exercicio7():
    import random

    numero = int(input("Número: "))
    nome = input("Nome do arquivo: ")
    arquivo = open(nome +".txt", "w")

    for i in range(1,numero + 1):
        arquivo.write(str(random.randint(1,1001)) + "\r\n")

    arquivo.close()
    menu()

def exercicio8():
    nome = input("Nome do arquivo: ")
    linhas = [int(i) for i in getLinesFromFile(nome)]
    linhas.sort()
    
    count = len(linhas)
    media = sum(linhas) / count

    if count % 2 == 0:
        ind1 = int(count / 2 - 1)
        ind2 = int(count / 2 + 1)
        mediana = sum(linhas[ind1:ind2])/2
    else:
        ind = int(count / 2)
        mediana = linhas[ind]
        
    print("Média:", media, "Mediana:", mediana)
    menu()
    
def exercicio9():
    nome = input("Nome do arquivo: ")
    dias = int(input("Intervalo de dias: "))
    linhas = [int(i) for i in getLinesFromFile(nome)]
    length = len(linhas)

    if dias < length:

        for i in range(0,length - 1):

            if i >= dias:
                ini = i - dias
                fim = ini + dias
                lista_intervalo = linhas[ini:fim]
                lista_intervalo.sort()

                if dias % 2 == 0:
                    ind1 = int(dias / 2 - 1)
                    ind2 = int(dias / 2 + 1)
                    mediana = sum(lista_intervalo[ind1:ind2])/2
                else:
                    ind = int(dias / 2)
                    mediana = lista_intervalo[ind]
                #print("Valor pra conferir", linhas[i],"Calcular Mediana", lista_intervalo, "Mediana =", mediana)
                if linhas[i] >= (mediana*2): 
                    print("Notificação do dia", i+1,"com gasto de", linhas[i])
            
    else:
        print("O intervalo de dias tem que ser menor que o numero de despesas")

    menu()
    
def exercicio10():
    string1 = input("Primeira stirng: ")
    string2 = input("Segunda stirng: ")
    similaridade = 0
    for i in string1:
       if string2.count(i) > 0:
           similaridade += 1
    print("Similaridade de", similaridade)
    
    menu()
    

def getLinesFromFile(filename):
    arquivo = open(filename +".txt")
    linhas = [i.strip() for i in arquivo.readlines()]
    arquivo.close()
    return linhas
menu()