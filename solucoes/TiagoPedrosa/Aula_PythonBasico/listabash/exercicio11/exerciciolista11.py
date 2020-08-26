import os.path
import sys
from classes import *


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

def listaRegistros():
    pessoa = Pessoa()
    produto = Produto()
    compra = Compra()
    produtocompra = ProdutoCompra()

    pessoa.listar()
    produto.listar()
    compra.listar()
    produtocompra.listar()

menu()