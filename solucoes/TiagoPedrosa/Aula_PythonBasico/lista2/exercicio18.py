def funcCountChar():
    arquivo = open("she.txt", "r")
    conteudo = arquivo.read()
    caracters = set(conteudo.replace('\n', '').strip())

    for i in caracters:
        frequencia = conteudo.count(i)
        print("A frequência de", i.upper(), "é", frequencia)

    arquivo.close()
    
funcCountChar()