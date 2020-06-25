# coding: utf-8
#
# Exemplo da videoaula Python #22.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

try:
    # Abre o arquivo para leitura
    arquivo = open("lista.txt", "r")

    # Armazena as linhas em uma lista
    linhas = arquivo.readlines()

    # Percorre cada ítem da lista e exibe na tela com o número da linha
    i = 1
    for linha in linhas:
        linha = linha.strip()   # Remove o \n no final da linha
        print(f"Linha {i}: {linha}")
        i += 1

except FileNotFoundError:
    print("Arquivo não encontrado.")

except PermissionError:
    print("Sem permissão para abrir o arquivo.")
    
except IOError:
    print("Erro de E/S.")

else:
    # Fecha o arquivo
    arquivo.close()
