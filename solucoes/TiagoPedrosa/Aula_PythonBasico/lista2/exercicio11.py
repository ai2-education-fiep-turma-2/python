def numPrim():
    limite = (int(input("Limite: ")))
    
    for i in range(0,limite + 1):
        count = 0
        for divisor in range(1, i):
            if i % divisor == 0:
                count = count + 1
                if count > 1:
                    break
        if count == 1:
            print(i)
   

numPrim()