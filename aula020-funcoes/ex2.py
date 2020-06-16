# coding: utf-8
#
# Exemplo da videoaula Python #20.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

def ola(*nomes):
    for pessoa in nomes:
        print(f"Olá, {pessoa}")

ola("João", "Pedro", "Maria", "Fernanda")
