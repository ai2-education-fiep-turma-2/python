def valueSort():
    dicionario = {'x': 1, 'y': 2, 'a': 3}
    sorteddici = []

    for i in sorted(dicionario):
        sorteddici.append(dicionario[i])
    print(sorteddici)

    
valueSort()