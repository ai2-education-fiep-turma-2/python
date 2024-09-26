def funcReverse():
    arquivo = open("she.txt")
    linhas = arquivo.readlines()

    for line in reversed(linhas):
        print(line)
        
    arquivo.close()
    
funcReverse()