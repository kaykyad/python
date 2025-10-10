def classificacaoAparelho(inmetro):
    match inmetro:
        case ("A"):
            print(f"Muito eficiente")
        case ("B"):
            print(f"Eficiente")
        case ("C"):
            print(f"Pouco eficiente")
        case ("D"):
            print(f"Ineficiente")
        case _:
            print(f"Inmetro {inmetro} não foi encontrado ")


def main():
    print("Digite a letra do inmetro: ")
    inmetro = str(input())

    classificacaoAparelho(inmetro)

if __name__ == "__main__":
    main()