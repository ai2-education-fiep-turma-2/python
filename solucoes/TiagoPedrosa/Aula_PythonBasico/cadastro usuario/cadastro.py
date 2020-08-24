def generateID(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i + 1

def cadastro():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    userid = generateID("usuario.txt")
    
    newline = str(userid) + "," + nome + "," + idade + "," + sexo + "\n" 

    cadastroFile = open("usuario.txt", "a")
    cadastroFile.write(newline)
    cadastroFile.close()
    menu()

def listar():
    cadastroFile = open("usuario.txt", "r")
    for line in cadastroFile: 
        print(line)
    
    cadastroFile.close()
    menu()

def sair():
    import sys
    sys.exit()
    

def menu():
    option = int(input("Digite 1 para cadastrar, 2 para listar e 3 para sair "))

    if (option == 1):
        cadastro()
    elif (option == 2):
        listar()
    elif (option == 3):
        sair()
    else:
        print("Não foi um comando valido")
    
menu()
