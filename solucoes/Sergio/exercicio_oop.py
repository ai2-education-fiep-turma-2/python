class texto:
    def __init__(self, nome_arquivo):
        self.lista_string = []
        self.arquivo = open(nome_arquivo, "r")
        self.stop_words = []

    def cadastra_stop_words(self):
        continuar = "S"
        while (continuar == "S"):
            self.stop_words.append(input("Digite uma Stop Word: ")+ " ")
            continuar = input("Deseja continuar? (S p/ sim e N p/ Não)")
        print(self.stop_words)

    def excluir_stop_words(self):
        self.arquivo = open("shakespeare.txt", "r")
        linhas = self.arquivo.readlines()
        arquivo_stop_words = open("arquivo_sem_stop_words.txt", "w+")

        for linha in linhas:
            linha_stop_words = linha.lower()
            for s in self.stop_words:
                linha_stop_words = linha_stop_words.replace(s, '')

            linha_teste = ""
            arquivo_stop_words.write(linha_teste.join(linha_stop_words))

    def distancia_entre_palavras(self, palavra_1, palavra_2):
        self.arquivo = open("shakespeare.txt", "r")
        linhas = self.arquivo.readlines()
        num_linha_1 = 0
        num_linha_2 = 0
        cont = 0

        for linha in linhas:
            if palavra_1 in linha:
                num_linha_1 = cont

            if palavra_2 in linha:
                num_linha_2 = cont

            cont += 1
            if (num_linha_1 != 0 and num_linha_2 != 0):
                    break

        print(palavra_1)
        print(str(num_linha_1))
        print(palavra_2)
        print(str(num_linha_2))
        print("A distância entre as palavras é de " + str(abs(num_linha_1 - num_linha_2)) + " linhas")

    def separar_por_palavra(self):
        if (self.arquivo.mode == 'r'):
            conteudo = self.arquivo.read()
            self.lista_string = conteudo.split(" ")

    def imprime_lista_string(self):
        self.remove_pontuacao()
        print("\n".join(self.lista_string))

    def remove_pontuacao(self):
        self.lista_string  = ([s.translate(str.maketrans('','','\n.,!;?[]()')) for s in self.lista_string])
        self.lista_string = ([s.lower() for s in self.lista_string])

    def ocorrencias_por_palavra(self):
        self.contador = dict()
        self.remove_pontuacao()

        for palavra in self.lista_string:
            if palavra in self.contador:
                self.contador[palavra] += 1
            else:
                self.contador[palavra] = 1

        for chave, item in self.contador.items():
            print(str(chave) + " - " + str(item))

    def palavras_mais_frequentes(self):
        lista_ordenada = sorted(self.contador.items(), key=lambda x: x[1], reverse=True)

        for i in range(11):
            print(str(lista_ordenada[i]) + " \n")

    def calculos(self):
        soma = 0
        for chave, item in self.contador.items():
            soma += item

        media = soma/len(self.contador)
        print("A média é de " + str(media) + " ocorrências por palavra.")

        soma = 0
        for chave, item in self.contador.items():
            soma += (item - media)**2
        dp = (soma/len(self.contador))**(1/2)
        print("O desvio padrão foi de " + str(dp))

novo_texto = texto(input("Digite o nome do arquivo: "))
novo_texto.separar_por_palavra()
#novo_texto.imprime_lista_string()
novo_texto.ocorrencias_por_palavra()
novo_texto.palavras_mais_frequentes()
novo_texto.calculos()
novo_texto.cadastra_stop_words()
novo_texto.excluir_stop_words()
novo_texto.distancia_entre_palavras(input("Digite a primeira palavra:"), input("Digite a segunda palavra:"))
