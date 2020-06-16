# coding: utf-8
#
# Exemplo da videoaula Python #20.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

def menu(*opcoes):
    i = 0
    
    for op in opcoes:
        print(f"{i}: {op}")
        i += 1
    
    try:
        return int(input(f"Escolha uma opção: "))
    except ValueError:
        return -1

resposta = menu("Adicionar", "Exibir", "Remover", "Sair")

if resposta == -1:
    print("Opção inválida.")
else:
    print(f"Opção escolhida foi {resposta}.")
