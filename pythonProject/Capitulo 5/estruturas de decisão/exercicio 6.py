def numeroParOuImpar(numero):
    if numero % 2 != 0:
      print(f"O {numero} é impar")
    else:
      print(f"O {numero} é par")


numero = int(input("Escreva um numero: "))

numeroParOuImpar(numero)