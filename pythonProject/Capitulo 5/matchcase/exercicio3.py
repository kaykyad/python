def verificaFeriado(mes, dia):
    match mes:
        case 9:
            match dia:
                case 7:
                     print(f"Dia {dia} é independência do Brasil!")
        case 10:
            match dia:
                case 12:
                   print(f"Dia {dia} é dia das crianças.")
                case _:
                    print(f"Este dia não existe")
        case _:
            print("Esse mes não existe")

def main():
  dia = int(input("Digite o dia do mês: "))
  mes = int(input("Digite um mês: "))

  verificaFeriado(mes, dia)

if __name__ == "__main__":
    main()