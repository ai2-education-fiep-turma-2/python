import os.path
import sys
from classes import *


def menu():
    option = int(input("Digite: \n 1 - Cadastrar usuário,\n 2 - Cadastrar produto,\n 3 - Cadastrar compra,\n 4 - Cadastrar produto da compra,\n 5 - Mostrar a média de idade\n 0  - Sair "))

    if (option == 1):
        cadastroPessoa()
    elif (option == 2):
        cadastroProduto()
    elif (option == 3):
        cadastroCompra()
    elif (option == 4):
        cadastroProdutoCompra()
    elif (option == 5):
        mostrarMediaIdade()
    elif (option == 10):
        listaRegistros()
    elif (option == 0):
        sair()
    else:
        print("Não foi um comando valido")

def sair():
    sys.exit()


def cadastroPessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    
    pessoa = Pessoa()
    pessoa.cadstrar(nome,idade,sexo)   
    menu()

def cadastroProduto():
    nome = input("Nome: ")
    valor = input("Valor: ")
    tamanho = input("Tamanho: ")
    
    produto = Produto()
    produto.cadstrar(nome,valor,tamanho)
    menu()

def cadastroCompra():
    id_usuario = input("ID do usuário: ")
    data = input("Data: ")
    
    compra = Compra()
    compra.cadstrar(id_usuario,data)
    menu()

def cadastroProdutoCompra():
    id_compra = input("ID da compra: ")
    id_produto = input("ID do produto: ")
    quantidade = input("Quantidade: ")

    produtocompra = ProdutoCompra()
    produtocompra.cadstrar(id_compra,id_produto,quantidade)
    menu()


def mostrarMediaIdade():
    pessoa = Pessoa()
    print("Média de idade:", pessoa.getMediaIdade())

def listaRegistros():
    pessoa = Pessoa()
    produto = Produto()
    compra = Compra()
    produtocompra = ProdutoCompra()

    print(pessoa.listar())
    print(produto.listar())
    print(compra.listar())
    print(produtocompra.listar())

    

menu()