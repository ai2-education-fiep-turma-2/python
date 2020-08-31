from csv import reader
from collections import Counter

class Aeroportos:

    def __init__(self, path):
        self.__path = path
        self.__data = self.open()

    def open(self):
        with open(self.__path, encoding="utf8") as arq_csv:
            leitor_csv = reader(arq_csv, delimiter=';')
            lista_csv = list(leitor_csv)
        return lista_csv
    """
    1.2) Extrair número de atrasos, recebendo como parâmetro, o ano de referência, 
    e.g.: ./flight-delays -n 2006 deve listar o número de vôos com atraso em 2006.
    def atrasos(self):
    """
    def atrasos(self, ano):
        contador = 0
        len_coluna = len(self.__data[0:])   
        if self.__data[1][0] == ano:
            for i in range(1, len_coluna):
                if self.__data[i][14] == 'NA':
                    contador = contador                
                elif int(self.__data[i][14]) > 0:
                    contador += 1
        return contador
    """
    1.3) Mostrar lista de companhias aéreas que sofreram atraso, recebendo como parâmetro o ano de referência
    Utilizar o arquivo carriers.csv
    """
    def companhias_atrasos_comprida(self, path_carriers, ano):
             
        f = open(path_carriers, "r")
        data = f.readlines()
        f.close()

        # Tira as aspas do arquivo carriers e cria uma matriz (data) do conteúdo do arquivo
        # data[i][0] = código da companhia = coluna 'UniqueCarrier' do arquivo 2006.csv
        # data[i][1] = nome da companhia
        for i in range(len(data)):
            data[i] = data[i].replace('\n' , '').replace('"', "").split(",")
        
        # Cria uma lista (companhias) do conteúdo da coluna 8 = 'UniqueCarrier' do arquivo ano.csv 
        # contendo só as COMPANHIAS QUE SOFRERAM ATRASO 
        # essa coluna 8 possui o código da companhia
        companhias = []
        
        len_coluna = len(self.__data[0:])   
        # Comprova se o ano ingressado é igual ao ano do arquivo
        if self.__data[1][0] == ano:
            for i in range(1, len_coluna):
                if self.__data[i][14] != 'NA' and int(self.__data[i][14]) > 0:
                    companhias.append(self.__data[i][8])        
        
        # Se o código da companhia que sofreu atraso (companhias) for igual
        # ao código da lista carriers, é adicionado um novo elemento na lista_companhias, contendo
        # o nome do aeroporto que sofreu atraso

        lista_companhias = []
      
        if len(data) > len(companhias):

            for i in range (len(companhias)):
                for j in range (len(data)):
                    if companhias[i] == data[j][0]:
                        lista_companhias.append(data[j][1])
        else:

            for i in range (len(data)):
                for j in range (len(companhias)):
                    if data[i] == companhias[j][0]:
                        lista_companhias.append(companhias[j][1])

        return lista_companhias
        
    # Elimina os elementos repetidos da lista_companhias

    def companhias_atrasos_pequena(self, path_carriers, ano):
        
        x = Aeroportos(self.__path)
        lista_companhias = x.companhias_atrasos_comprida(path_carriers, ano)

        i = 0
        while i < len(lista_companhias):
            j = i + 1
            while j < len(lista_companhias):
                if lista_companhias[j] == lista_companhias[i]:
                    del(lista_companhias[j])
                else:
                   j += 1
            i += 1

        return lista_companhias

    """
    1.4) Mostrar a lista de Aeroportos com atrasos, recevendo como parâmetro o ano de referência
    Utilizar o arquivo airports.csv
    Criar nova issue que altere a funcionalidade de download de dataset para também baixar esse arquivo
    """       
    # Quase igual ao exercício 3), diferença: pega a coluna 15 da matriz self.__data em lugar da 14

    def aeroportos_atrasos_comprida(self, path_airports, ano):
    
        f = open(path_airports, "r")
        data = f.readlines()
        f.close()

        # Tira as aspas do arquivo 'airports' e cria uma matriz (data) do conteúdo do arquivo
        # data[i][0] = iata
        # data[i][1] = airport
        # data[i][2] = city
        # data[i][3] = state 
        # ...
        # data[i][6] = long

        for i in range(len(data)):
            data[i] = data[i].replace('\n' , '').replace('"', "").split(",")
        
        # Cria uma lista (aeroportos) do conteúdo da coluna 16 = 'Origin' do arquivo ano.csv 
        # contendo só os códigos dos AEROPORTOS que SOFRERAM ATRASO 
        # essa coluna 16 possui o código do aeroporto em que decolou o avião

        aeroportos = []
        
        len_coluna = len(self.__data[0:])   
        # Comprova se o ano ingressado é igual ao ano do arquivo
        if self.__data[1][0] == ano:
            for i in range(1, len_coluna):
                if self.__data[i][15] != 'NA' and int(self.__data[i][15]) > 0:
                    aeroportos.append(self.__data[i][16])    
        
        # Se o código do aeroporto que sofreu atraso (aeroportos) for igual
        # ao código do aeroporto na lista 'airports' (coluna 0 da matriz data), é adicionado um novo elemento na lista_aeroporots, 
        # contendo o nome do aeroporto que sofreu atraso

        lista_aeroportos = []
      
        if len(data) > len(aeroportos):

            for i in range (len(aeroportos)):
                for j in range (len(data)):
                    if aeroportos[i] == data[j][0]:
                        lista_aeroportos.append(data[j][1])
        else:

            for i in range (len(data)):
                for j in range (len(aeroportos)):
                    if data[i] == aeroportos[j][0]:
                        lista_aeroportos.append(aeroportos[j][1])
        
        return lista_aeroportos

    # Elimina os elementos repetidos da lista_aeroportos

    def aeroportos_atrasos_pequena (self,path_airports,ano):
        
        x = Aeroportos(self.__path)
        
        lista_aeroportos = x.aeroportos_atrasos_comprida(path_airports,ano)

        i = 0
        while i < len(lista_aeroportos):
            j = i + 1
            while j < len(lista_aeroportos):
                if lista_aeroportos[j] == lista_aeroportos[i]:
                    del(lista_aeroportos[j])
                else:
                   j += 1
            i += 1

        return lista_aeroportos
    
    """
    2.1) Contabilizar o número de atrasos ocorridos em cada aeroporto, 
    listando o nome do aeroporto em uma coluna e o número de atrasos na segunda coluna (recebendo como parâmetro o ano base)
    """  
    def num_atrasos_aeroporto(self, path_airports, ano):

        #Puxando o resultado do exercício 1.4
        x = Aeroportos(self.__path)
        lista_aeroporotos_comprida = x.aeroportos_atrasos_comprida(path_airports,ano)
        
        # Conta as ocorrencias de cada aeroporto na lista_aeroportos (versão comprida) 
        # e retorna um dicionário

        num_atrasos = dict(Counter(lista_aeroporotos_comprida))

        return num_atrasos
    """
    2.2) Contabilizar o número de atrasos ocorridos em cada companhia aérea, 
    listando o nome da companhia em uma coluna e o número de atrasos na segunda coluna (recebendo como parâmetro o ano base)
    """
    def num_atrasos_companhia(self, path_carriers, ano):
        #Puxando o resultado do exercício 1.3
        x = Aeroportos(self.__path)
        lista_companhias_comprida = x.companhias_atrasos_comprida(path_carriers,ano)
        
        # Conta as ocorrencias de cada companhia na lista_companhias (versão comprida) 
        # e retorna um dicionário

        num_atrasos = dict(Counter(lista_companhias_comprida))

        return num_atrasos
    """
    2.3) Listar qual companhia teve o maior número de atrasos (atrasos somente na decolagem).
    """

    """
    extra) Mostra a lista de companhias aéreas que sofreram atraso NO DEPARTURE, recebendo como parâmetro o ano de referência
    Utilizar o arquivo carriers.csv
    """
    def companhias_atrasos_departure(self, path_carriers, ano):

        f = open(path_carriers, "r")
        data = f.readlines()
        f.close()

        # Tira as aspas do arquivo carriers e cria uma matriz (data) do conteúdo do arquivo
        # data[i][0] = código da companhia = coluna 'UniqueCarrier' do arquivo 2006.csv
        # data[i][1] = nome da companhia
        for i in range(len(data)):
            data[i] = data[i].replace('\n' , '').replace('"', "").split(",")
        
        # Cria uma lista (companhias) do conteúdo da coluna 8 = 'UniqueCarrier' do arquivo ano.csv 
        # contendo só as COMPANHIAS QUE SOFRERAM ATRASO NO DEPARTURE
        # essa coluna 8 possui o código da companhia
        companhias = []
        
        len_coluna = len(self.__data[0:])   
        # Comprova se o ano ingressado é igual ao ano do arquivo
        if self.__data[1][0] == ano:
            for i in range(1, len_coluna):
                if self.__data[i][15] != 'NA' and int(self.__data[i][15]) > 0:
                    companhias.append(self.__data[i][8])        
        
        # Se o código da companhia que sofreu atraso NO DEPARTURE (companhias) for igual
        # ao código da lista carriers, é adicionado um novo elemento na lista_companhias, contendo
        # o nome do aeroporto que sofreu atraso

        lista_companhias = []
      
        if len(data) > len(companhias):

            for i in range (len(companhias)):
                for j in range (len(data)):
                    if companhias[i] == data[j][0]:
                        lista_companhias.append(data[j][1])
        else:

            for i in range (len(data)):
                for j in range (len(companhias)):
                    if data[i] == companhias[j][0]:
                        lista_companhias.append(companhias[j][1])

        return lista_companhias
    
    def companhia_mais_atrasos(self, path_carriers, ano):

        #Puxando o resultado da função acima
        x = Aeroportos(self.__path)
        companhias_atrasos_departures = x.companhias_atrasos_departure(path_carriers,ano)
        
        # Conta as ocorrencias de cada aeroporto na lista_aeroportos (versão comprida) 
        # e retorna um dicionário

        num_atrasos = dict(Counter(companhias_atrasos_departures))

        num_maior_atrasos = list(num_atrasos.items())
      
        return num_maior_atrasos[0]


        
        

#x = Aeroportos('2006.csv')
y = Aeroportos('teste_2006.csv')
# x.open()
# a = y.atrasos('2006')
# a = y.companhias_atrasos_comprida('carriers.csv', '2006')
# a = y.companhias_atrasos_pequena('carriers.csv', '2006')

# a = y.aeroportos_atrasos_comprida('airports.csv', '2006')
# b = y.aeroportos_atrasos_pequena('airports.csv', '2006')
# print(b)
# a = y.num_atrasos_aeroporto('airports.csv', '2006')
# a = y.num_atrasos_companhia('carriers.csv', '2006')

# a = y.companhias_atrasos_departure('carriers.csv', '2006')
# b = y.companhias_atrasos_comprida('carriers.csv', '2006')
# print(a)
# print(b)
a = y.companhia_mais_atrasos('carriers.csv', '2006')
print(a)
