def calculaQuantidadePares(numero1, numero2, numero3, numero4):
    quantidadePar = 0

    if(numero1 % 2 == 0):
        quantidadePar += 1
    if(numero2 % 2 == 0):
        quantidadePar += 1
    if (numero3 % 2 == 0):
        quantidadePar += 1
    if (numero4 % 2 == 0):



numero1 = int(input("Digíte O primeiro numero"))
numero2 = int(input("Digíte O segundo numero"))
numero3 = int(input("Digíte O terceiro numero"))
numero4 = int(input("Digíte O quarto numero"))

quantidadeNumerosPares = calculaQuantidadePares(numero1, numero2, numero3, numero4)