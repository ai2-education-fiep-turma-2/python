def funcProd():
    from math import prod
    limite = (int(input("Tamanho da lista: ")))

    produto = prod(range(1,limite + 1))
    print("O produto é:", produto)
        
   
funcProd()