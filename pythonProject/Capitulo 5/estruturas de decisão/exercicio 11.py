def classificacaoProduto(numeroDoCodigo):
    if numeroDoCodigo == 1:
        print("Classificação: Alimento não-perecível")
    elif 2 <= numeroDoCodigo <= 4:
        print("Classificação: Alimento perecível")
    elif 5 <= numeroDoCodigo <= 6:
        print("Classificação: Vestuário")
    elif numeroDoCodigo == 7:
        print("Classificação: Higiene pessoal")
    elif 8 <= numeroDoCodigo <= 15:
        print("Classificação: Limpeza e utensílios domésticos")
    else:
        print("Codigo invalido")

numeroDoCodigo = int(input("Digite o codigo: "))

classificacaoProduto(numeroDoCodigo)