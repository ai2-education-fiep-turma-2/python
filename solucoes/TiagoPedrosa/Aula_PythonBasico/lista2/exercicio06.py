def speedCheck():
    speed = int(input("Velocidade do motorista: "))

    if (speed < 70):
        print("Ok")
    else:
        pontos = 0
        count = 0
        for i in range(70,speed):
            count += 1           
            if (count % 5 == 0):
                pontos += 1
            if (pontos > 12):
                print("Licen suspended")
                return
        print("Pontos: ", pontos)

speedCheck()