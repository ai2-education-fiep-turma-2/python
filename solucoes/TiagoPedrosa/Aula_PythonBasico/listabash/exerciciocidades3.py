def sortCity():
    arquivo = open("cidades.txt")
    linhas = arquivo.readlines()

    new_arq = open("arq2.txt", "w") 

    for i in linhas[11:13]:
        new_arq.write(i) 

    new_arq.close() 


sortCity()
