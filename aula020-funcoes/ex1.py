# coding: utf-8
#
# Exemplo da videoaula Python #20.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

def titulo(texto, enfeite = "+", quantidade = 3):
    print(f"{enfeite}" * quantidade, end = "")
    print(f" {texto} ", end = "")
    print(f"{enfeite}" * quantidade)

titulo("teste 1")
titulo("teste 2", "o")
titulo("teste 3", "-", 5)

titulo("teste 4", quantidade = 5)
