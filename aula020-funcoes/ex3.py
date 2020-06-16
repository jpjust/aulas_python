# coding: utf-8
#
# Exemplo da videoaula Python #20.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

def soma(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s

total = soma(1, 10)
print(f"A soma de todos os números de 1 até 10 é {total}.")
