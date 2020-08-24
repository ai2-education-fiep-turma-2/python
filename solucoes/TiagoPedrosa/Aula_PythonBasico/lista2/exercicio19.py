def funcAnagram():
    lista = ['eat', 'ate', 'done', 'tea', 'soup', 'node', 'eac', 'teste', 'tstee']
    newlist = []

    for i in lista:
        #verifica se a palavra da vez já esta na nova lista, para evitar repetir os anagramas
        if len([x for x in newlist if i in x]) > 0:
            continue
        #pegar as palavras do mesmo tamanho
        mesmotamanho = [palavra for palavra in lista if len(palavra) == len(i)]
        acc = []
        #percorrer cada palavra da lista de palavras com o mesmo tamanho
        for w in mesmotamanho:
            count = 0
            for letra in i:
                #verifica se a palavra tem a letra que esta no loop
                if (w.count(letra) > 0):
                    count +=1
            #verifica se as letras bateram com a palavra
            if (count == len(i)):  
                acc.append(w)
        #criando nova lista
        newlist.append(acc)

    print(newlist)

  

    
funcAnagram()