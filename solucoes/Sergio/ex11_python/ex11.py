import datetime
lista_usuarios = {}
lista_produtos = {}
lista_vendas = {}

class Usuario:
    def __init__(self, id_usuario, nome_usuario, idade_usuario, sexo_usuario):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.idade_usuario = idade_usuario
        self.sexo_usuario = sexo_usuario

        lista_usuarios[id_usuario] = self

    def __str__(self):
        return str("<"+self.id_usuario+","+self.nome_usuario+","+self.idade_usuario+","+self.sexo_usuario+">")

    def gravar_usuario(self):
        f= open("cadastro_usuario.txt","a")
        f.write(self.id_usuario+","+self.nome_usuario+","+self.idade_usuario+","+self.sexo_usuario+"\n")

class Produto:
    def __init__(self, id_produto, valor_produto, tamanho_produto):
        self.id_produto = id_produto
        self.valor_produto = valor_produto
        self.tamanho_produto = tamanho_produto

        lista_produtos[id_produto] = self

    def __str__(self):
        return str("<"+self.id_produto+","+self.valor_produto+","+self.tamanho_produto+">")

    def gravar_produto(self):
        f= open("cadastro_produto.txt","a")
        f.write(self.id_produto+","+self.valor_produto+","+self.tamanho_produto+"\n")

class Venda:
    def __init__(self, id_venda, usuario, hora_venda, nova_venda):
        self.id_venda = id_venda
        self.usuario = usuario
        self.hora_venda = hora_venda

        self.produtos_venda = []
        if(nova_venda):
            self.produtos_venda = cadastro_produto_venda(id_venda)
        else:
            self.produtos_venda = carrega_produtos_venda(id_venda)

        lista_vendas[id_venda] = self

    def __str__(self):
        return str("<"+self.id_venda+","+self.usuario.id_usuario+","+self.hora_venda+">")

    def gravar_venda(self):
        f= open("cadastro_venda.txt","a")
        f.write(self.id_venda+","+self.usuario.id_usuario+","+self.hora_venda+"\n")

class Produto_Venda:
    def __init__(self, id_venda, produto, quantidade):
        self.id_venda = id_venda
        self.produto = produto
        self.quantidade = quantidade

    def gravar_produto_venda(self):
        f= open("cadastro_produto_vendas.txt","a")
        f.write(self.id_venda+","+self.produto.id_produto+","+self.quantidade+"\n")

def cadastro_usuario():
    print("Cadastro de Clientes:\n")
    id_usuario = input("Digite o id do usuário (2 digitos), seguido de [ENTER]:")
    nome_usuario = input("Digite o nome do usuário, seguido de [ENTER]:")
    idade_usuario = input("Digite a idade do usuário (2 digitos), seguido de [ENTER]:")
    sexo_usuario = input("Digite o sexo do usuário (Masculino, Feminino ou Outros), seguido de [ENTER]:")

    usuario = Usuario(id_usuario, nome_usuario, idade_usuario, sexo_usuario)
    usuario.gravar_usuario()

def cadastro_produto():
    print("Cadastro de Produtos:\n")
    id_produto = input("Digite o id do Produto (2 digitos), seguido de [ENTER]:")
    valor_produto = input("Digite o valor do Produto, seguido de [ENTER]:")
    tamanho_produto = input("Digite o tamanho do Produto (em metros), seguido de [ENTER]:")

    produto = Produto(id_produto, valor_produto, tamanho_produto)
    produto.gravar_produto()

def cadastro_venda():
    print("Cadastro de Vendas: \n")
    id_venda = input("Digite o id para a compra (2 digitos), seguido de [ENTER]:")
    id_usuario_venda = input("Digite o id do usuário que realizou a compra (2 digitos), seguido de [ENTER]:")

    usuario = lista_usuarios[id_usuario_venda]
    data_atual = datetime.datetime.now()
    hora_venda = data_atual.hour
    if(hora_venda > 12):
        hora_venda = hora_venda - 12
    venda = Venda(id_venda, usuario, str(hora_venda), True)
    venda.gravar_venda()

def cadastro_produto_venda(id_venda):
    print( "Produtos Venda: \n")

    produtos_venda = []
    cadastrar_novo_produto = "S"
    while(cadastrar_novo_produto == "S"):

        id_venda_local = id_venda
        id_produto_venda = input("Digite o id para o produto (2 digitos), seguido de [ENTER]:")
        produto = lista_produtos[id_produto_venda]
        quantidade = input("Digite a quantidade de produtos, seguido de [ENTER}:")

        produto_venda = Produto_Venda(id_venda_local, produto, quantidade)
        produto_venda.gravar_produto_venda()
        produtos_venda.append(produto_venda)

        cadastrar_novo_produto = input("Deseja cadastrar outro produto? (S p/ Sim e N p/ Não)")
    return produtos_venda

def media_quantidade_usuario():
    for i in range(len(lista_usuarios)):
        usuario = lista_usuarios["{0:0=2d}".format(i+1)]
        soma = 0
        cont = 0
        for venda in lista_vendas.values():
            if (venda.usuario.id_usuario == usuario.id_usuario):
                for produto_venda in venda.produtos_venda:
                    soma += float(produto_venda.quantidade)
                    cont += 1
        if (cont == 0):
            cont = 1
        print("A média de quantidade de compra do usuário: "+ usuario.nome_usuario + " foi de " + str(soma/cont) + "\n")

def media_valor_usuario():
    for i in range(len(lista_usuarios)):
        usuario = lista_usuarios["{0:0=2d}".format(i+1)]
        soma = 0
        cont = 0
        for venda in lista_vendas.values():
            if (venda.usuario.id_usuario == usuario.id_usuario):
                for produto_venda in venda.produtos_venda:
                    soma += (float(produto_venda.produto.valor_produto) * float(produto_venda.quantidade))
                    cont += float(produto_venda.quantidade)
        if (cont == 0):
            cont = 1
        print("A média de gastos do usuário: "+ usuario.nome_usuario + " foi de " + str(soma/cont) + "\n")

def media_valor_categoria():
    soma = {"masculino":0 , "feminino":0, "outros":0}
    cont = {"masculino":0 , "feminino":0, "outros":0}

    for venda in lista_vendas.values():
        for produto_venda in venda.produtos_venda:
            soma[venda.usuario.sexo_usuario] = soma[venda.usuario.sexo_usuario] + (float(produto_venda.produto.valor_produto) * float(produto_venda.quantidade))
            cont[venda.usuario.sexo_usuario] = cont[venda.usuario.sexo_usuario] + float(produto_venda.quantidade)

    for chave, item in soma.items():
        if (cont[chave] == 0):
            cont[chave] = 1
        print("A categoria " +chave+ " tem media de " + str(item/cont[chave]))

def media_valor_horario():
    soma = {"8":0 ,"9":0 ,"10":0 ,"11":0 ,"12":0,"1":0 ,"2":0 ,"3":0 ,"4":0 ,"5":0 ,"6":0 ,"7":0}
    cont = {"8":0 ,"9":0 ,"10":0 ,"11":0 ,"12":0,"1":0 ,"2":0 ,"3":0 ,"4":0 ,"5":0 ,"6":0 ,"7":0}

    for venda in lista_vendas.values():
        for produto_venda in venda.produtos_venda:
            soma[venda.hora_venda] = soma[venda.hora_venda] + (float(produto_venda.produto.valor_produto) * float(produto_venda.quantidade))
            cont[venda.hora_venda] = cont[venda.hora_venda] + float(produto_venda.quantidade)

    print("\n\n Horário de funcionamento: 8-12 (am) e 1-7(pm) \n\n")
    for chave, item in soma.items():
        if (cont[chave] == 0):
            cont[chave] = 1
        print("O horário " +chave+ " tem media de " + str(item/cont[chave]))

def calculos_e_filtros():
    print("-Cálculos e Filtros- \n\n")
    print("1- Média de quantidade de produtos por usuário")
    print("2- Média de valor gasto por usuário")
    print("3- Média de valor por categoria de usuário")
    print("4- Valor média de compra por horário")
    opcao = input()
    if(opcao == "1"):
        media_quantidade_usuario()
    elif(opcao == "2"):
        media_valor_usuario()
    elif(opcao == "3"):
        media_valor_categoria()
    elif(opcao == "4"):
        media_valor_horario()
    else:
        print("opção inválida")

def carrega_usuarios():
    arquivo = open("cadastro_usuario.txt", "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        usuario = linha.split(",")
        Usuario(usuario[0], usuario[1], usuario[2], usuario[3].replace("\n", ""))

def carrega_produtos():
    arquivo = open("cadastro_produto.txt", "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        produto = linha.split(",")
        Produto(produto[0], produto[1], produto[2].replace("\n", ""))

def carrega_vendas():
    arquivo = open("cadastro_venda.txt", "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        venda = linha.split(",")
        Venda(venda[0], lista_usuarios[venda[1]], venda[2].replace("\n", ""), False)

def carrega_produtos_venda(id_venda):
    arquivo = open("cadastro_produto_vendas.txt", "r")
    linhas = arquivo.readlines()
    lista_produtos_venda = []
    for linha in linhas:
        produtos_venda = linha.split(",")
        if(produtos_venda[0] == id_venda):
            produto_venda = Produto_Venda(produtos_venda[0], lista_produtos[produtos_venda[1]], produtos_venda[2].replace("\n", ""))
            lista_produtos_venda.append(produto_venda)

    return lista_produtos_venda

def carregar_listas():
    carrega_usuarios()
    carrega_produtos()
    carrega_vendas()

def mostra_cadastros():

    print("\n Usuários: \n")
    print("id_usuario, nome_usuario, idade_usuario, sexo_usuario \n")
    for usuario in lista_usuarios.values():
        print(usuario)

    print("\n Produtos: \n")
    print("id_produto, valor_produto, tamanho_produto \n")
    for produto in lista_produtos.values():
        print(produto)

    print("\n Vendas: \n")
    print("id venda, id_usuario, hora_venda \n")
    for venda in lista_vendas.values():
        print(venda)

carregar_listas()
continuar = "s"
while(continuar == "s"):
    print("-Software de Gestão- \n\n")
    print("1- Cadastro de usuário")
    print("2- Cadastro de produtos")
    print("3- Cadastro de vendas")
    print("4- Cálculos")
    print("5- Ver Cadastros")
    opcao = input()
    if(opcao == "1"):
        cadastro_usuario()
    elif(opcao == "2"):
        cadastro_produto()
    elif(opcao == "3"):
        cadastro_venda()
    elif(opcao == "4"):
        calculos_e_filtros()
    elif(opcao == "5"):
        mostra_cadastros()
    else:
        print("opção inválida")

    continuar = input(" \n\n Deseja continuar? (s p/ sim e n p/ Não)")
