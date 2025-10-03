def divisaoPorCinco (numero):
    if numero % 5 == 0:
        print(f"O {numero} pode ser dividido por 5")
    else:
        print(f"O {numero} não pode ser dividido por 5")

def divisaoPorTres(numero):
    if numero % 3 == 0:
        print(f"O {numero} pode ser dividido por 3")
    else:
        print(f"O {numero} não pode ser dividido por 3")


numero = int(input("Digite seu numero inteiro: "))

divisaoPorCinco(numero)
divisaoPorTres(numero)
