def sortCity():
    arquivo = open("cidades.txt")
    linhas = arquivo.readlines()

    new_arq = open("arq1.txt", "w") 

    for i in sorted(linhas, key=str.casefold):
        new_arq.write(i) 

    new_arq.close() 


sortCity()
