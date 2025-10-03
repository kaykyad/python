def classificacaoDoJogador(idade):
    if idade < 5:
        print("Não tem idade ")
    elif 5 <= idade <= 7:
        print("Sua classificação esta no infantil A ")
    elif 8 <= idade <= 10:
        print("Sua classificação esta no infantil B ")
    elif 11 <= idade <= 13:
        print("Sua classificação esta no juvenil A ")
    elif 14 <= idade <= 17:
        print("sua classificação esta no juvenil B ")



idade = int(input("Digite sua idade: "))

classificacaoDoJogador(idade)