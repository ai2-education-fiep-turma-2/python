def funcWrap():
    limite = int(input("Limite da linha: "))
    arquivo = open("she.txt")
    linhas = arquivo.readlines()

    for line in linhas:
        newline = line[:limite] + '\n' + line[limite:]
        print(newline)

    arquivo.close()
    
funcWrap()