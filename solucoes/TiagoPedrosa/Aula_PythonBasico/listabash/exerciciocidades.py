def analisaCidades():
    arquivo = open("cidades.txt")
    linhas = [i.strip().lower() for i in arquivo.readlines()]
    unique = set(linhas)


    for i in unique:
        frequencia = linhas.count(i)
        print("A frequência de", i.upper(), "é", frequencia)
    
    print("Cidades total:", len(linhas), ", Cidades unicas: ", len(unique))
analisaCidades() 