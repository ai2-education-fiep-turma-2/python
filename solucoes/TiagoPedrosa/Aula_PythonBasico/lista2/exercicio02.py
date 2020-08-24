def doarSangue():
    idade = int(input("Informe sua idade: "))
    peso = float(input("Informe seu peso: "))
    sono = float(input("Informe quantas horas dormidas nas últimas 24h: "))

    if (idade < 16 or idade > 69):
        print("Para doar sangue é preciso ter entre 16 e 69 anos.")
        return
    if (peso < 50):
        print("Para doar sangue é preciso pesar mais de 50 kg.")
        return
    if (sono < 6):
        print("Para doar sangue é preciso ter dormido pelo menos 6 horas nas últimas 24 horas.")
        return
    
    print("Você está apto para doar sangue!")

doarSangue()