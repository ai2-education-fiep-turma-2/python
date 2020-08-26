import os.path
import sys

class Basic():
    def generateID(self, filename):
        if os.path.isfile(filename):     
            with open(filename) as f:
                for i,l in enumerate(f):                 
                    pass
            return str(i + 2)
        else:
            return str(1)

    def insertFile(self, line, filename):
        cadastroFile = open(filename, "a")
        cadastroFile.write(line)
        cadastroFile.close()
    
    def getFile(self, filename):
        cadastroFile = open(filename, "r")
        for line in cadastroFile: 
            print(line)
        
        cadastroFile.close()

class Pessoa(Basic):

    def cadstrar(self, nome, idade, sexo):
        id = self.generateID("usuario.txt")
        newline = id + "," + nome + "," + idade + "," + sexo + "\n" 
        self.insertFile(newline,"usuario.txt")

    def listar(self):
        self.getFile("usuario.txt")

class Produto(Basic):

    def cadstrar(self, nome, valor, tamanho):
        id = self.generateID("produto.txt")
        newline = id + "," + nome + "," + valor + "," + tamanho + "\n" 
        self.insertFile(newline,"produto.txt")

    def listar(self):
        self.getFile("produto.txt")

class Compra(Basic):

    def cadstrar(self, id_usuario, data):
        id = self.generateID("nota_fiscal.txt")
        newline = id + "," + id_usuario + "," + data + "\n" 
        self.insertFile(newline,"nota_fiscal.txt")

    def listar(self):
        self.getFile("nota_fiscal.txt")


class ProdutoCompra(Basic):

    def cadstrar(self, id_compra, id_produto, quantidade):
        id = self.generateID("nota_fiscal_produto.txt")
        newline = id + "," + id_compra + "," + id_produto + "," + quantidade + "\n"  
        self.insertFile(newline,"nota_fiscal_produto.txt")

    def listar(self):
        self.getFile("nota_fiscal_produto.txt")