def concatena_texto(texto1, texto2):
    texto_inteiro = texto1 + texto2
    imprime_2_vezes(texto_inteiro)

def imprime_2_vezes(texto_inteiro):
    print(texto_inteiro)
    print(texto_inteiro)

texto1 = "agua mole em pedra dura "
texto2 = "tanto bate ate que fura."

concatena_texto(texto1, texto2)