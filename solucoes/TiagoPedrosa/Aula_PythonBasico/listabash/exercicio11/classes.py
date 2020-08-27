import os.path
import sys

class Basic():
    def __init__(self):
        self.path = ""
    
    def generateID(self):
        if os.path.isfile(self.path):     
            with open(self.path) as f:
                for i,l in enumerate(f):                 
                    pass
            return str(i + 2)
        else:
            return str(1)

    def insertFile(self, line):
        cadastroFile = open(self.path, "a")
        cadastroFile.write(line)
        cadastroFile.close()
        
    def getFile(self):
        cadastroFile = open(self.path, "r")
        conteudo = cadastroFile.read()
        
        cadastroFile.close()
        return conteudo

    def getListLinhas(self):
        listLinhas = []
        cadastroFile = open(self.path, "r")
        for line in cadastroFile: 
            listLinhas.append(line.replace("\n","").split(","))
        cadastroFile.close()

        return listLinhas


class Pessoa(Basic):
    def __init__(self):
        self.path = "usuario.txt"

    def cadstrar(self, nome, idade, sexo):
        id = self.generateID()
        newline = id + "," + nome + "," + idade + "," + sexo + "\n" 
        self.insertFile(newline)

    def listar(self):
        linhas = self.getFile()
        return linhas

    def getMediaIdade(self):
        listaLinhas = self.getListLinhas()
        count = len(listaLinhas)
        listaIdades = [int(i[2]) for i in listaLinhas]
        media = round(sum(listaIdades) / count,2)
        return media

class Produto(Basic):
    def __init__(self):
        self.path = "produto.txt"

    def cadstrar(self, nome, valor, tamanho):
        id = self.generateID()
        newline = id + "," + nome + "," + valor + "," + tamanho + "\n" 
        self.insertFile(newline)

    def listar(self):
        linhas = self.getFile()
        return linhas

class Compra(Basic):
    def __init__(self):
        self.path = "nota_fiscal.txt"

    def cadstrar(self, id_usuario, data):
        id = self.generateID()
        newline = id + "," + id_usuario + "," + data + "\n" 
        self.insertFile(newline)

    def listar(self):
        linhas = self.getFile()
        return linhas


class ProdutoCompra(Basic):
    def __init__(self):
        self.path = "nota_fiscal_produto.txt"

    def cadstrar(self, id_compra, id_produto, quantidade):
        id = self.generateID()
        newline = id + "," + id_compra + "," + id_produto + "," + quantidade + "\n"  
        self.insertFile(newline)

    def listar(self):
        linhas = self.getFile()
        return linhas