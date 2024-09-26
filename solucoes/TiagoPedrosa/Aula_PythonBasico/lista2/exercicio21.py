def changeKeyValue():
    dicionario = {'x': 1, 'y': 2, 'a': 3}
    novodicionario = {}

    for key,value in dicionario.items():
        novodicionario[value] = key
    print(novodicionario)

    
changeKeyValue()