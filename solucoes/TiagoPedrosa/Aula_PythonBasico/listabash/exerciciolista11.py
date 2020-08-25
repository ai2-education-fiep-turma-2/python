import os.path
import sys

def generateID(fname):
    if os.path.isfile(fname):
        with open(fname) as f:
            for i,l in enumerate(f):
                pass
        return i + 1
    else:
        return 1
        
def cadastroPessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    userid = generateID("usuario.txt")
    
    newline = str(userid) + "," + nome + "," + idade + "," + sexo + "\n" 

    cadastroFile = open("usuario.txt", "a")
    cadastroFile.write(newline)
    cadastroFile.close()
    menu()

def cadastroProduto():
    nome = input("Nome: ")
    valor = input("Valor: ")
    tamanho = input("Tamanho: ")
    prodid = generateID("produto.txt")
    
    newline = str(prodid) + "," + nome + "," + valor + "," + tamanho + "\n" 

    cadastroFile = open("produto.txt", "a")
    cadastroFile.write(newline)
    cadastroFile.close()
    menu()

def cadastroCompra():
    id_usuario = input("ID do usuário: ")
    data = input("Data: ")
    idcompra = generateID("nota_fiscal.txt")
    
    newline = str(idcompra) + "," + id_usuario + "," + data + "\n" 

    cadastroFile = open("nota_fiscal.txt", "a")
    cadastroFile.write(newline)
    cadastroFile.close()
    menu()

def cadastroProdutoCompra():
    id_compra = input("ID da compra: ")
    id_produto = input("ID do produto: ")
    quantidade = input("Quantidade: ")
    
    newline = id_compra + "," + id_produto + "," + quantidade + "\n" 

    cadastroFile = open("nota_fiscal_produto.txt", "a")
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
    sys.exit()
    

def menu():
    option = int(input("Digite 1 para cadastrar usuário, 2 para cadastrar produto, 3 para cadastrar compra, 4 para cadastrar produto da compra e 0 para sair "))

    if (option == 1):
        cadastroPessoa()
    elif (option == 2):
        cadastroProduto()
    elif (option == 3):
        cadastroCompra()
    elif (option == 4):
        cadastroProdutoCompra()
    elif (option == 0):
        sair()
    else:
        print("Não foi um comando valido")
    
menu()
