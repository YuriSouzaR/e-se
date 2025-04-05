a = str(input("Vamos ao mencado ? sim/nao \n "))
if a == "nao":
    print("Está bem! \n caso queira testar nosso programa favor Reinicie!!")
    a2 = str(input("Deseja reiniciar ? sim/nao "))
    if a2 == "sim":
        print("Ok.. Reiniciando")

if a == "sim":
    print("esta bem...")

b = str(input("Vamos fazer uma lista de 5 alimentos ! \n Escolha 5 alimentos:  "))
c = str(input(""))
d = str(input(""))
e = str(input(""))
f = str(input(""))
print("LISTA: ")
alm = list()
alm.append(b)
alm.append(c)
alm.append(d)
alm.append(e)
alm.append(f)
print(alm)
g = str(input("deseja colocar mais algum alimento na lista ? \n "))
if g == "sim":
    print("Está bem !")
    g1 = int(input("Deseja colocar quantos alimentos em sua lista ? \n"))
    for cont in range(0, g1):
        alm.append(str(input("Qual alimento você deseja ? \n ")))
    print(f"Lista atualizada ! \n sua lista agora é : {alm}")
if g == "nao" or "sim":
    i = int(input("OK.. Escolha uma dessas coisas para fazer agora: \n 1-Ir para o caixa pagar. \n 2-Escolher mais algum alimento. \n 3-Sair sem pagar. \n 4-Ficar parado. \n"))

if i == 1:
    print("Você pagou os Alimentos e foi para casa!")
    print("Teste as outras Escolhas!")

if i == 2:
    j = int(input("Deseja quantos alimentos ?"))
    for cont in range(0, j):
            alm.append(str(input(f"Escolha mais {j - 1} alimentos : \n")))
    print(f"Lista atualizada novamente! \n Sua lista agora é : {alm}")
    k = int(input("OK.. Escolha uma dessas coisas para fazer agora: \n 1-Ir para o caixa pagar. \n 2-Escolher mais algum alimento. \n 3-Sair sem pagar. \n 4-Ficar parado. \n "))
    if k == 1:
        print("Você pagou os Alimentos e foi para casa!")
        print("Teste as outras Escolhas!")

    if k == 2:
        m = int(input("Deseja quantos alimentos ?"))
        for cont in range(0, j):
            alm.append(str(input(f"Escolha mais {j - 1} alimentos : \n")))
        print(f"Lista atualizada novamente! \n Sua lista agora é : {alm}")
    if k == 3:
        print("VOCÊ FOI PRESO POR TENTATIVA DE ROUBO!!")
        a1 = int(input("Você está na prisão.. Oque fazer ? \n 1-Tentar fugir. 2-Não fugir. \n "))
        if a1 == 1:
            print(
                "A fuga foi um SUCESSO! \n Junto com você fugiu 2 colegas de cela \n Você mudou de estado (para nao ser capturado pois você está sendo procurado) \n Você começou uma nova vida !!")
            print("POR ENQUANTO É ISSO.. AINDA ESTOU DESENVOLVENDO!")

    if k == 4:
        n = str(input(
            "Você ficou parado! \n Eventualmente o mercado foi Fecahdo e as Luzes apagadas!! \n Por sorte seu celular estava com a bateria cheia (97%) e você usa a Lanterna \n Oque fazer agora ? \n 1-Explorar. \n 2-Se esconder ate amanhecer. \n "))
        if n == 1:
            print("Você explora o local! \n Acaba encontrando uma Lanterna!")
            o = str(input("Você pega a Lanterna ? Sim/Nao \n "))
            if o == "sim":
                print("VOCÊ ADIQUIRIU UM OBJETO !! \n ===Lanterna===")
                inv = list("Lanterna")
                print("-Você utiliza a lanterna para economizar a bateria de seu celular-")
                p = int(input("Oque fazer agora ? \n (1)Continuar explorando  ou (2)Se esconder ate amanhecer ? \n"))
                print("!!!!POR ENQUANTO É ISSO.. AINDA VOU TERMINAR DE DESENVOLVER!!!!")

if i == 3:
    print("VOCÊ FOI PRESO POR TENTATIVA DE ROUBO!!")
    a1 = int(input("Você está na prisão.. Oque fazer ? \n 1-Tentar fugir. 2-Não fugir. \n "))
    if a1 == 1:
        print("A fuga foi um SUCESSO! \n Junto com você fugiu 2 colegas de cela \n Você mudou de estado (para nao ser capturado pois você está sendo procurado) \n Você começou uma nova vida !!")
        print("POR ENQUANTO É ISSO.. AINDA ESTOU DESENVOLVENDO!")

if i == 4:
    l = int(input("Você ficou parado! \n Eventualmente o mercado foi Fechado e as Luzes apagadas!! \n Por sorte seu celular estava com a bateria cheia (97%) e você usa a Lanterna \n Oque fazer agora ? \n 1-Explorar. \n 2-Se esconder ate amanhecer. "))
    if l == 1:
        print("Você explora o local! \n Acaba encontrando uma Lanterna!")
        o = str(input("Você pega a Lanterna ? Sim/Nao \n "))
        if o == "sim":
            print("VOCÊ ADIQUIRIU UM OBJETO !! \n ===Lanterna===")
            inv = list("Lanterna")
            print("-Você utiliza a lanterna para economizar a bateria de seu celular-")
            p = int(input("Oque fazer agora ? \n (1)Continuar explorando  ou (2)Se esconder ate amanhecer ? \n"))
            print("!!!!POR ENQUANTO É ISSO.. AINDA VOU TERMINAR DE DESENVOLVER!!!!")
