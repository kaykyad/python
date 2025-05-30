def mostrar_nome_inteiro(nome, sobreNome):
    print(nome)
    sobreNome(sobreNome)

def sobreNome(sobreNome):
    print(sobreNome)


nome = "Jose"
sobreNome = "Valim"
mostrar_nome_inteiro(nome, sobreNome)