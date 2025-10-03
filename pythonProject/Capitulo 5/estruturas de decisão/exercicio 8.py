def divisaoPorDois (numero):
    if numero % 2 == 0:
        print(f"O {numero} pode ser dividido por 2")
    else:
        print(f"O {numero} não pode ser dividido por 2")

def divisaoPorTres(numero):
    if numero % 2 == 0:
        print(f"O {numero} pode ser dividido por 3")
    else:
        print(f"O {numero} não pode ser dividido por 3")


numero = int(input("Digite seu numero inteiro: "))

divisaoPorDois(numero)
divisaoPorTres(numero)
