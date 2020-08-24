def showStars():
    times = int(input("Informe o número: "))
    print("```")
    for i in range(1,times + 1):
        for l in range(i):
            print("*", end=" ")
        print("")
    print("```")
showStars()