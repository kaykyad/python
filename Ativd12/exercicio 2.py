def soma(numero, numero2):
   print("o resultado da soma é:", numero + numero2)


def subtracao(numero, numero2):
   print("o resultado da subtração é:", numero - numero2)


def multiplicacao(numero, numero2):
   print("o resultado da multiplicacao é:", numero * numero2)

def divisao(numero, numero2):
    resultado_divisao = numero / numero2
    print("O resultado da divisao é: ", resultado_divisao)


numero = int(input("digite o 1° numero:"))
numero2 = int(input("digite o 2° numero:"))


soma(numero, numero2)
subtracao(numero, numero2)
multiplicacao(numero, numero2)
divisao(numero, numero2)