#torre de hanói

haste01 = [4, 3, 2, 1]
haste02 = []
haste03 = []

hasteLista = [haste01, haste02, haste03]

while True:

    #mostrar no display
    print("\n1 -", haste01)
    print("2 -", haste02)
    print("3 -", haste03)

    print("")
    print("//" * 20)

    while True:

        #determinar haste de saída
        hasteSaida = input("\nDigite o número da haste de SAÍDA: ")

        try:
            hasteSaida = int(hasteSaida)

            if not 1 <= hasteSaida <= 3:
                print("\nInsira um valor entre 1 e 3")
                continue

        except:
            print("\nValor inválido!!!")
            continue


        #determinar haste de entrada
        hasteEntrada = input("\nDigite o número da haste de ENTRADA: ")

        try:
            hasteEntrada = int(hasteEntrada)

            if not 1 <= hasteEntrada <= 3:
                print("\nInsira um valor entre 1 e 3")
                continue

        except:
            print("\nValor inválido!!!")
            continue


        #verificar se as hastes são diferentes
        if hasteSaida == hasteEntrada:
            print("\nA haste de saída e a haste de entrada devem ser diferentes!")
            continue


        #transformar os números nas próprias listas
        hasteSaida = hasteLista[hasteSaida - 1]
        hasteEntrada = hasteLista[hasteEntrada - 1]


        #verificar se a haste de saída está vazia
        if len(hasteSaida) == 0:
            print("\nA haste de saída está vazia!")
            continue


        #identificar o disco que será movimentado
        discoSaida = hasteSaida[-1]


        #verificar se a haste de entrada está vazia
        if len(hasteEntrada) == 0:

            hasteEntrada.append(hasteSaida[-1])
            hasteSaida.pop(-1)

        #verificar se o disco pode ser colocado sobre o outro
        elif discoSaida < hasteEntrada[-1]:

            hasteEntrada.append(hasteSaida[-1])
            hasteSaida.pop(-1)

        #movimento inválido
        else:

            print("\nMovimento inválido!")
            continue

        break