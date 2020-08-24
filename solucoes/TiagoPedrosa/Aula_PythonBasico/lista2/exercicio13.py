def funcSumString():
    palavra1 = (input("Primeira palavra: "))
    palavra2 = (input("Segunda palavra: "))
    
    lista = [palavra1,palavra2]
    soma = "".join(lista)
    print("A junção das palavras é:", soma)
        
   
funcSumString()