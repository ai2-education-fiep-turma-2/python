def monthName():
    mes = int(input("Digite o número do mês: "))
    if (mes > 0 and mes < 13):
        nome_mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        print(nome_mes[mes - 1])
    else:
        print("Não existe mês com esse número!")
monthName()